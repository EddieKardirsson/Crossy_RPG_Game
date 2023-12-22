import pygame


class GameObject:

    # To maintain the scalability and resolution independence, following will differ from the course's logic:
    #   * width and height if set to 0, it will get the image-file's corresponding width and height
    #   * scale_factor default value is 1 (mainly for background that doesn't need any scaling due to it
    #       using the display height as width and height value)
    #   * scale_factor is used for the other game objects to be scaled with.
    def __init__(self, x, y, width, height, image_path, scale_factor=1):
        image = pygame.image.load(image_path)
        self.scale_factor = scale_factor
        if width == 0 and height == 0:
            width = image.get_width() * scale_factor
            height = image.get_height() * scale_factor
        self.image = pygame.transform.scale(image, (width,
                                                    height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height
