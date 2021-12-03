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
    #
    # This is an array of tuples. The first parameter is the absorption coefficient, then the
    # second parameter is the speed of sound in that material.
    tissue_params = [
        (0, 0),        # Empty space
        (0.9, 1476),   # Fat
        (0.54, 1580),  # Muscle
        (0.66, 1564),  # Tumor
        (1.1, 1630)    # Nerve
    ]

    # Transmitted intensity formula
    def transmit(self, Z1, Z2):
        T_I = 4*Z1*Z2/((Z1 + Z2)**2)
        self.intensity *= T_I
        return self.intensity, T_I

    # Reflected intensity
    def reflect(self, Z1, Z2):
        R_I = (Z2-Z1)**2/((Z2+Z1)**2)
        self.intensity *= R_I
        return self.intensity, R_I

    # Propagation, mu is in units of dB/(cm*MHz)
    def propagate(self, mu, z):
        new_mu = mu / 4.343 * self.carrier_frequency
        self.intensity *= np.exp(-new_mu*z)
        return self.intensity

    def gen_image(self, subject):
        image = subject
        for x in range(len(subject)):
            for y in range(len(subject[x])):
                image[x][y] *= np.random.rayleigh()  # Speckle
                image[x][y] += np.random.normal(scale=self.noise_std_dev)  # Electronic Noise

        return image
