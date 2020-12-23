import pygame 
import time

class ScreenManager:

    """
    Constructor
    """
    def __init__(self, screen, white, player1, player2):
        self.screen = screen
        self.white = white
        self.black = (0, 0, 0)
        self.grey = (128, 128, 128)
        self.player1 = player1 
        self.player2 = player2
        self.big_font = pygame.font.Font('freesansbold.ttf', 32)
        self.small_font = pygame.font.Font('freesansbold.ttf', 14)

    """
    Display the start menu on the screen for 8 seconds
    """
    def display_start_menu(self):
        start_time = current_time = current_time = int(round(time.time()))
        
        while start_time + 8 >= current_time: ##====================================================================================================== 8
            self.screen.fill(self.white)

            # First to 5 text
            first_to_5 = self.big_font.render("First to 5 goals wins", True, self.black, self.white)
            first_to_5_rect = first_to_5.get_rect()
            first_to_5_rect.center = (250, 150)
            self.screen.blit(first_to_5, first_to_5_rect)

            # Player 1 controls
            p1_controls = self.small_font.render("Player 1 Controls: Move left: A. Move right: D", True, self.player1.colour, self.white)
            self.display_text(p1_controls, 250, 300)

            # Player 2 controls
            p2_controls = self.small_font.render("Player 2 Controls: Move left: LEFT ARROW. Move right: RIGHT ARROW", True, self.player2.colour, self.white)
            self.display_text(p2_controls, 250, 450)

            # Exit program if player presses exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            current_time = int(round(time.time()))
            pygame.display.update()


    """
    Display which player has won on the screen for 3 seconds
    """
    def display_player_has_won(self):
        start_time = current_time = int(round(time.time()))

        while start_time + 3 >= current_time:
            self.display_scores()

            # Player 1 wins
            if self.player1.score == 5:
                p1_win = self.big_font.render("Player 1 Wins", True, self.player1.colour, self.white)
                self.display_text(p1_win, 250, 300)

            # Player 2 wins
            if self.player2.score == 5:
                p2_win = self.big_font.render("Player 2 Wins", True, self.player2.colour, self.white)
                self.display_text(p2_win, 250, 300)

            current_time = int(round(time.time()))
            pygame.display.update() 

    """
    Display the score of each player on the screen
    """
    def display_scores(self):
        p1_score = self.big_font.render(str(self.player1.score), True, self.grey, self.white)
        self.display_text(p1_score, 450, 100)
        p2_score = self.big_font.render(str(self.player2.score), True, self.grey, self.white)
        self.display_text(p2_score, 450, 500)    

    """
    Display the text given on the screen at the given coordinates
    """
    def display_text(self, text, x, y):
        rect = text.get_rect()
        rect.center = (x, y)
        self.screen.blit(text, rect)            
            