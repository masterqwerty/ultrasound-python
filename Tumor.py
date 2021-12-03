import numpy as np

# Numbers inside the image:
#
# 0 - Empty space
# 1 - Fat
# 2 - Muscle
# 3 - Tumor
# 4 - Nerve


class Tumor:
    points_per_axis = 600
    fat_radius = (250, 225)
    muscle_radius = (225, 50)
    tumor_radius = 50
    nerve_radius = 25

    def __init__(self, distance):
        # We'll have 100 points per cm, showing [-3,3] cm on the plot.
        self.image = np.zeros((self.points_per_axis, self.points_per_axis))

        self.nerve_center = (300 + self.tumor_radius + self.nerve_radius + (distance * 100), 300)
        # Put the circle of the arm in the middle. Fill with fat.
        for x in range(self.points_per_axis):
            for y in range(self.points_per_axis):
                if self.is_nerve(x, y):
                    self.image[x][y] = 4
                elif self.is_fat(x, y):
                    self.image[x][y] = 1
                elif self.is_muscle(x, y):
                    self.image[x][y] = 2
                elif self.is_tumor(x, y):
                    self.image[x][y] = 3

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
