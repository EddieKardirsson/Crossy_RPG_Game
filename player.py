from gameObject import GameObject


class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed, scale_factor=1):
        super().__init__(x, y, width, height, image_path, scale_factor)

        self.speed = speed

    def move(self, direction):
        self.y += (direction * self.speed)
