import pygame
import player
import puck
import time

# Initialise pygame, screen and caption
pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Air Hockey")

# Colours and font
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
grey = (128, 128, 128)
blue = (0, 0, 255)
font = pygame.font.Font('freesansbold.ttf', 32)

# Initialise players and puck
p1_win = font.render("Player 1 Wins", True, red, white)
player1 = player.Player(200, 20, 100, 20, red, p1_win)
p2_win = font.render("Player 2 Wins", True, blue, white)
player2 = player.Player(200, 560, 100, 20, blue, p2_win)
puck = puck.Puck(250, 300, 20)

def display_start_menu(white):
    start_font = pygame.font.Font('freesansbold.ttf', 14)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(white)

    # First to 5 text
    first_to_5 = font.render("First to 5 goals wins", True, black, white)
    first_to_5_rect = first_to_5.get_rect()
    first_to_5_rect.center = (250, 150)
    screen.blit(first_to_5, first_to_5_rect)

    # Player 1 controls
    p1_controls = start_font.render("Player 1 Controls: Move left: A. Move right: D", True, black, white)
    player1.display_controls(screen, p1_controls, 300)

    # Player 2 controls
    p2_controls = start_font.render("Player 2 Controls: Move left: LEFT ARROW. Move right: RIGHT ARROW", True, black, white)
    player2.display_controls(screen, p2_controls, 450)

    pygame.display.update()

# Initialise global variables
display_text = False
start_time = int(round(time.time() * 1000))

# Display the start menu for 8 seconds 
running = False
while not running:
    display_start_menu(white)
    current_time = int(round(time.time() * 1000))
    if start_time + 8000 <= current_time:
        running = True

# =============================== MAIN GAMEPLAY ===============================
while running:

    # Set white screen
    screen.fill(white)

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display scores
    player1.display_scores(screen, font, grey, white, 100)
    player2.display_scores(screen, font, grey, white, 500)

    # Place players and puck on screen
    player1.draw(screen)
    player2.draw(screen)
    puck.draw(screen)

    # Move puck
    puck.move(player1, player2)

    # Detect player movement
    keys = pygame.key.get_pressed()

    # Player 1
    if keys[pygame.K_a]:
        player1.move_left() 
    if keys[pygame.K_d]:
        player1.move_right() 

    # Player 2
    if keys[pygame.K_LEFT]:
        player2.move_left() 
    if keys[pygame.K_RIGHT]:
        player2.move_right() 

    # Check to see if a player has won
    if player1.score == 5 or player2.score == 5:
        display_text = True
        start_time = int(round(time.time() * 1000))
    
    # Update display
    pygame.display.update()

    # Display who wins game for 2 seconds and then restart game
    while display_text:

        player1.display_scores(screen, font, grey, white, 100)
        player2.display_scores(screen, font, grey, white, 500)

        if player1.score == 5:
            player1.display_text(screen)

        if player2.score == 5:
            player2.display_text(screen)

        current_time = int(round(time.time() * 1000))
        if start_time + 2000 <= current_time:
            player1.restart(20)
            player2.restart(560)
            puck.reset()
            display_text = False

        pygame.display.update()