import UltraSound
import Arm
import matplotlib.pyplot as plt


def main():
    us = UltraSound.UltraSound(1, 5, 1, 1)
    arm = Arm.Arm(0.1)

    color_map = plt.imshow(arm.subject, extent=[-3, 3, -3, 3])
    plt.xlabel("cm")
    plt.ylabel("cm")
    color_map.set_cmap("Greys")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()
