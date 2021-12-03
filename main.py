import UltraSound
import Tumor
import matplotlib.pyplot as plt


def main():
    us = UltraSound.UltraSound(1, 5, 1, 1)
    tumor = Tumor.Tumor(0.1)

    plt.imshow(tumor.image)
    plt.colorbar()
    plt.show()
    # data = [[1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9]]
    # color_map = plt.imshow(data)
    # color_map.set_cmap("Greys_r")
    # plt.show()


if __name__ == "__main__":
    main()
