import numpy as np


class UltraSound:
    def __init__(self, arr_width, freq, axial, lateral):
        self.intensity = self.input_intensity
        self.array_width = arr_width
        self.carrier_frequency = freq  # MHz
        self.axial_res = axial * 10  # cm
        self.lateral_res = lateral * 10  # cm
        pass

    input_intensity = 0.1  # W/cm^2
    noise_std_dev = 0.001  # W/cm^2, Gaussian
    speckle_mean = 1  # Rayleigh Dist

    # Ultrasound parameters for the different tissues
    tissue_params = [
        {  # Empty space
            "density": 0,
            "absorption": 0,
            "speed": 0
        },
        {  # Fat
            "density": 0.6,
            "absorption": 0.9,
            "speed": 1476
        },
        {  # Muscle
            "density": 0.9,
            "absorption": 0.54,
            "speed": 1580
        },
        {  # Tumor
            "density": 0.8,
            "absorption": 0.66,
            "speed": 1564
        },
        {  # Nerve
            "density": 0.9,
            "absorption": 1.1,
            "speed": 1630
        }
    ]

    # Transmitted intensity formula
    def transmit(self, Z1, Z2):
        return 4 * Z1 * Z2 / ((Z1 + Z2) ** 2)

    # Reflected intensity
    def reflect(self, Z1, Z2):
        return (Z2 - Z1) ** 2 / ((Z2 + Z1) ** 2)

    # Propagation, mu is in units of dB/(cm*MHz)
    def propagate(self, mu, z):
        new_mu = mu / 4.343 * self.carrier_frequency
        self.intensity *= np.exp(-new_mu*z)
        return self.intensity

    def gen_image(self, subject):
        image = subject.copy()
        pixel_distance = 0.01  # cm
        for x in range(len(subject)):
            # Reset intensity
            self.intensity = self.input_intensity
            last_tissue = 0
            for y in range(len(subject[x])):
                current_tissue = int(subject[x][y])  # Get the tissue type

                # Calculate impedances.
                Z1 = self.tissue_params[last_tissue]["density"] * self.tissue_params[last_tissue]["speed"]
                Z2 = self.tissue_params[current_tissue]["density"] * self.tissue_params[current_tissue]["speed"]

                if current_tissue == 0 or last_tissue == 0:
                    image[x][y] = 0.01  # Ignore any empty space.
                else:
                    T_I = self.transmit(Z1, Z2)
                    R_I = self.reflect(Z1, Z2)
                    image[x][y] = T_I * self.intensity
                    self.propagate(self.tissue_params[current_tissue]["absorption"], pixel_distance)
                    # if last_tissue != current_tissue:
                    #     for yi in range(y+1):
                    #         if int(subject[x][yi]) != 0:
                    #             self.intensity *= R_I

                image[x][y] *= np.random.rayleigh()  # Speckle
                image[x][y] += np.random.normal(scale=self.noise_std_dev)  # Electronic Noise

                last_tissue = current_tissue

        # Now compute the image by taking averages based on axial and lateral resolutions.
        num_axial = int(len(subject) / self.axial_res)
        num_lateral = int(len(subject[0]) / self.lateral_res)

        final_image = np.zeros((num_axial, num_lateral))

        axial = int(self.axial_res)
        lateral = int(self.lateral_res)

        for i in range(num_axial):
            for j in range(num_lateral):
                i_start = i * axial
                i_end = (i + 1) * axial
                j_start = j * lateral
                j_end = (j + 1) * lateral
                data = image[i_start:i_end, j_start:j_end]
                final_image[i][j] = np.average(data)

        return final_image
