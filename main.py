import UltraSound
import Arm
import matplotlib.pyplot as plt


def main():
    us = UltraSound.UltraSound(1, 4, 0.2, 0.5)
    arm = Arm.Arm(0.1)

    image = us.gen_image(arm)
    # image = arm.subject

    color_map = plt.imshow(image, extent=[-3, 3, -3, 3])
    plt.xlabel("cm")
    plt.ylabel("cm")
    color_map.set_cmap("Greys_r")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()
