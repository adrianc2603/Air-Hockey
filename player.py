import pygame

class Player:

    """
    Constructor
    """
    def __init__(self, y, colour, screen):
        self.x = 200
        self.y = y
        self.width = 100
        self.height = 20
        self.velocity = 3
        self.colour = colour
        self.score = 0
        self.update_rectangle()
        self.screen = screen

    """
    Reset the player to its original position
    """
    def reset(self):
        self.x = 200
        self.update_rectangle()

    """
    Reset the player to its original position and score of 0
    """
    def restart(self):
        self.reset()
        self.score = 0

    """
    Move the player left if they are not at the edge of screen
    """
    def move_left(self):
        if self.x > 0:
            self.x -= self.velocity
            self.update_rectangle()

    """
    Move the player right if they are not at the edge of screen
    """
    def move_right(self):
        if (self.x + self.width) < 500:
            self.x += self.velocity
            self.update_rectangle()

    """
    Draw the player on the screen
    """
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))

    """
    Update the position of the player's rectangle
    """
    def update_rectangle(self):
        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
