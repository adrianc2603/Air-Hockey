import pygame
import player
import puck
import screen_manager

# Initialise pygame, screen and caption
pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Air Hockey")

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Initialise players and puck
player1 = player.Player(20, red, screen)
player2 = player.Player(560, blue, screen)
puck = puck.Puck(screen, player1, player2)

# Initialise screen manager
screen_manager = screen_manager.ScreenManager(screen, white, player1, player2)

# Display the start menu 
screen_manager.display_start_menu()

# =============================== MAIN GAMEPLAY ===============================

running = True
while running:

    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # User presses pause
    if keys[pygame.K_p]:
        screen_manager.display_paused()

    # Set white screen
    screen.fill(white)

    # Display scores
    screen_manager.display_scores()

    # Place players and puck on screen
    player1.draw()
    player2.draw()
    puck.draw()

    # Move puck
    puck.move()

    # Player 1 Moves
    if keys[pygame.K_a]:
        player1.move_left() 
    if keys[pygame.K_d]:
        player1.move_right() 

    # Player 2 Moves 
    if keys[pygame.K_LEFT]:
        player2.move_left() 
    if keys[pygame.K_RIGHT]:
        player2.move_right() 

    # Update display
    pygame.display.update()    

    # If game is won, display who wins game for 3 seconds and then restart game
    if player1.score == 5 or player2.score == 5:
        screen_manager.display_player_has_won()
        player1.restart()
        player2.restart()
        puck.reset()

    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    