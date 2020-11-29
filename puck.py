import pygame

class Puck:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius 
        self.colour = (0, 0, 0)
        self.x_speed = 0
        self.y_speed = 6

    def reset(self):
        self.x = 250
        self.y = 300
        self.x_speed = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)

    def goal_scored(self, player, player_y, other_player, other_y):
        player.score += 1
        player.reset(player_y)
        other_player.reset(other_y)
        self.reset()

    def collision_with_borders(self):
        if (self.x + self.radius) >= 500 or (self.x - self.radius) <= 0:
            self.x_speed *= -1

            if self.y_speed == 0:
                if self.y >= 300:
                    self.y_speed = -5
                else:
                    self.y_speed = 5

    def collision_with_player(self, player):
        if (self.x + self.radius) >= player.x and (self.x - self.radius) <= (player.x + player.width):

            # Hits the top of the player
            if (self.y - self.radius) == (player.y + player.height) or (self.y + self.radius) == player.y:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.x_speed = -2
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.x_speed = 2
                self.y_speed *= -1

            # Hits either side of the player        ## MAKE CHANGES HERE TO FIX BUG (2.5 <= PLAYER.X <= SELF.X)
            elif (self.y - self.radius) <= (player.y + player.height) and (self.y + self.radius) >= player.y:
                if (self.x - self.radius) == (player.x + player.width):
                    self.x_speed = 6
                    self.y_speed = 0

                if (self.x + self.radius) == player.x:
                    self.x_speed = -6
                    self.y_speed = 0

    def move(self, player1, player2):
        self.x += self.x_speed
        self.y += self.y_speed

        self.collision_with_borders()

        # Player 1 scores a point
        if (self.y + self.radius) >= 600:
            self.goal_scored(player1, 20, player2, 560)

        # Player 2 scores a point
        if (self.y - self.radius) <= 0:
            self.goal_scored(player2, 560, player1, 20)

        self.collision_with_player(player1)
        self.collision_with_player(player2)