import numpy as np


class Arm:
    points_per_axis = 600
    fat_radius = (250, 225)
    muscle_radius = (225, 50)
    tumor_radius = 50
    nerve_radius = 25

    # Ultrasound parameters for the different tissues
    #
    # This is an array of tuples. The first parameter is the absorption coefficient, then the
    # second parameter is the speed of sound in that material. The index corresponds to the
    # number of the tissue as defined in the comment before creating the image.
    us_parameters = [
        (0, 0),
        (0.9, 1476),
        (0.54, 1580),
        (0.66, 1564),
        (1.1, 1630)
    ]

    def __init__(self, distance):
        # We'll have 100 points per cm, showing [-3,3] cm on the plot.
        self.subject = np.zeros((self.points_per_axis, self.points_per_axis))

        self.nerve_center = (300 + self.tumor_radius + self.nerve_radius + (distance * 100), 300)

        # Numbers inside the image:
        #
        # 0 - Empty space
        # 1 - Fat
        # 2 - Muscle
        # 3 - Tumor
        # 4 - Nerve
        for x in range(self.points_per_axis):
            for y in range(self.points_per_axis):
                if self.is_nerve(x, y):
                    self.subject[x][y] = 4
                elif self.is_fat(x, y):
                    self.subject[x][y] = 1
                elif self.is_muscle(x, y):
                    self.subject[x][y] = 2
                elif self.is_tumor(x, y):
                    self.subject[x][y] = 3

    def is_fat(self, x, y):
        circle_radius = (x - self.points_per_axis / 2) ** 2 + (y - self.points_per_axis / 2) ** 2
        return self.fat_radius[0] ** 2 > circle_radius > self.fat_radius[1] ** 2

    def is_muscle(self, x, y):
        circle_radius = (x - self.points_per_axis / 2) ** 2 + (y - self.points_per_axis / 2) ** 2
        return self.muscle_radius[0] ** 2 > circle_radius > self.muscle_radius[1] ** 2

    def is_tumor(self, x, y):
        circle_radius = (x - self.points_per_axis / 2) ** 2 + (y - self.points_per_axis / 2) ** 2
        return circle_radius < self.tumor_radius ** 2

    def is_nerve(self, x, y):
        circle_radius = (x - self.nerve_center[0]) ** 2 + (y - self.nerve_center[1]) ** 2
        return circle_radius < self.nerve_radius ** 2
