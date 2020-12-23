import pygame

class Player:

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 3
        self.colour = colour
        self.score = 0

    def reset(self, y):
        self.x = 200
        self.y = y

    def restart(self, y):
        self.reset(y)
        self.score = 0

    def move_left(self):
        if self.x > 0:
            self.x -= self.velocity

    def move_right(self):
        if (self.x + self.width) < 500:
            self.x += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

   
   
   