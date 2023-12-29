from gameObject import GameObject


class Player(GameObject):

    def __init__(self, x, y, width, height, image_path, speed, scale_factor=1):
        super().__init__(x, y, width, height, image_path, scale_factor)

        self.speed = speed

    def move(self, direction_x, direction_y, min_width, max_width, max_height):
        if (((self.x >= max_width - self.width) and (direction_x > 0))
                or (self.x <= min_width) and (direction_x < 0)):
            return
        if (((self.y >= max_height - self.height) and (direction_y > 0))
                or (self.y <= 0) and (direction_y < 0)):
            return
        self.x += (direction_x * self.speed)
        self.y += (direction_y * self.speed)
