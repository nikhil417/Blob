import random


class Blob:

    def __init__(self, color, weidth, heigth, size_range=(4, 8), move_speed=(-1, 1)):
        self.weidth = weidth
        self.heigth = heigth
        self.x = random.randrange(0, self.weidth)
        self.y = random.randrange(0, self.heigth)
        self.size = random.randrange(size_range[0], size_range[1])
        self.move_speed = move_speed
        self.color = color

    def move(self):
        self.move_x = random.randrange(self.move_speed[0], self.move_speed[1])
        self.move_y = random.randrange(self.move_speed[0], self.move_speed[1])

        self.x += self.move_x
        self.y += self.move_y

        if self.x > self.weidth:
            self.x = 0
        elif self.x < 0:
            self.x = self.weidth

        if self.y > self.heigth:
            self.y = 0
        elif self.y < 0:
            self.y = self.heigth
