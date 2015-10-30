 
import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
 
#### What's good cam
## hey man
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create  screen size
screen = pygame.display.set_mode([800, 800])
 
# This sets the name of the window
pygame.display.set_caption('my latif')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:

# Set positions of graphics
background_position = [400, 400]
 
# Load and set up graphics.
background_image = pygame.image.load("ha.jpg").convert()
player_image = pygame.image.load("tb.gif").convert()
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    screen.blit(player_image, [x, y])
 
    pygame.display.flip()
 
    clock.tick(600)
 
pygame.quit()
