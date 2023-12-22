from gameObject import GameObject

class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed, scale_factor=1):
        super().__init__(x, y, width, height, image_path, scale_factor)

        self.speed = speed

    def move(self, boundaries):
        if self.x <= boundaries[0]:
            self.speed = abs(self.speed)
        elif self.x >= boundaries[1] - self.width * self.scale_factor:
            self.speed = -self.speed

        self.x += self.speed
