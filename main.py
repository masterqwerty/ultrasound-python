import UltraSound
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde


def main():
    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    color_map = plt.imshow(data)
    color_map.set_cmap("Greys_r")
    plt.show()


if __name__ == "__main__":
    main()
