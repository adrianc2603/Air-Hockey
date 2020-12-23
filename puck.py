import pygame

class Puck:

    """
    Constructor
    """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius 
        self.colour = (0, 0, 0) # Black
        self.x_speed = 0
        self.y_speed = 6
        self.rectangle = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    """
    Reset the puck to its original position
    """
    def reset(self):
        self.x = 250
        self.y = 300
        self.x_speed = 0

    """
    Draw the rectangle on the screen
    """
    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)

    """
    Update the position of the puck's rectangle
    """
    def update_rectange(self):
        self.rectangle = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    """
    Perform the functionality to move the puck and check if 
    it collides with anything
    """
    def move(self, player1, player2):
        self.x += self.x_speed
        self.y += self.y_speed

        self.update_rectange()
        self.collision_with_borders()
        self.collision_with_player(player1, player2)

        if self.goal_scored(player1, player2):
            player1.reset()
            player2.reset()
            self.reset()

    """
    Change direction of puck if it collides with borders
    """
    def collision_with_borders(self):
        if (self.x + self.radius) >= 500 or (self.x - self.radius) <= 0:
            self.x_speed *= -1

            if self.y_speed == 0:
                if self.y >= 300:
                    self.y_speed = -5
                else:
                    self.y_speed = 5

    
    """
    Change the direction of the puck if it collides with a player
    """
    def collision_with_player(self, player1, player2):
        keys = pygame.key.get_pressed()
        
        # Player 1
        if self.rectangle.colliderect(player1.rectangle):

            # Change x-direction depending on which direction player is moving
            if keys[pygame.K_a]:
                    self.x_speed = -2
            if keys[pygame.K_d]:
                self.x_speed = 2   

            self.y_speed *= -1    

        # Player 2
        if self.rectangle.colliderect(player2.rectangle):

            # Change x-direction depending on which direction player is moving
            if keys[pygame.K_LEFT]:
                    self.x_speed = -2
            if keys[pygame.K_RIGHT]:
                self.x_speed = 2 

            self.y_speed *= -1 

    """
    If a player scores a goal, increase their score and return True.
    Return False otherwise
    """
    def goal_scored(self, player1, player2):

        # Player 1 scores a point
        if (self.y + self.radius) >= 600:
            player1.score += 1
            return True

        # Player 2 scores a point
        if (self.y - self.radius) <= 0:
            player2.score += 1
            return True

        return False                       
