import pygame

class Player:

    def __init__(self, x, y, width, height, colour, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 3
        self.colour = colour
        self.score = 0
        self.text = text

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

    def display_controls(self, screen, text, y):
        rect = text.get_rect()
        rect.center = (250, y)
        screen.blit(text, rect)

    def display_scores(self, screen, font, colour, background_colour, y):
        score = font.render(str(self.score), True, colour, background_colour)
        score_rect = score.get_rect()
        score_rect.center = (450, y) 
        screen.blit(score, score_rect)

    def display_text(self, screen):
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (250, 300)
        screen.blit(self.text, self.text_rect)