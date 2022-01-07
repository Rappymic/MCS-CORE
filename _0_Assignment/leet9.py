import random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        self.max_x = self.radius + self.x
        self.max_y = self.radius + self.y
        self.min_x = self.radius - self.x
        self.min_y = self.radius - self.y
        a = random.uniform(self.min_x, self.max_x)
        b = random.uniform(self.min_y, self.max_y)
        return [a,b]

 