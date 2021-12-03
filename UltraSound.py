import numpy as np


class UltraSound:
    def __init__(self, arr_width, freq, axial, lateral):
        self.intensity = self.input_intensity
        self.array_width = arr_width
        self.carrier_frequency = freq  # MHz
        self.axial_res = axial
        self.lateral_res = lateral
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
        image = subject
        pixel_distance = 0.01  # cm
        for x in range(len(subject)):
            # Reset intensity
            self.intensity = self.input_intensity
            last_tissue = 0
            for y in range(len(subject[x])):
                current_tissue = int(image[x][y])  # Grab the number before we put the intensity in.

                # Calculate impedances.
                Z1 = self.tissue_params[last_tissue]["density"] * self.tissue_params[last_tissue]["speed"]
                Z2 = self.tissue_params[current_tissue]["density"] * self.tissue_params[current_tissue]["speed"]

                if current_tissue == 0 or last_tissue == 0:
                    image[x][y] = self.input_intensity  # Ignore any empty space.
                else:
                    T_I = self.transmit(Z1, Z2)
                    R_I = self.reflect(Z1, Z2)
                    image[x][y] = T_I * self.propagate(self.tissue_params[current_tissue]["absorption"], pixel_distance)

                # image[x][y] *= np.random.rayleigh()  # Speckle
                # image[x][y] += np.random.normal(scale=self.noise_std_dev)  # Electronic Noise

                last_tissue = current_tissue

        return image
