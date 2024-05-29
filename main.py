import pygame
import player

pygame.init()
screen_height = 768
screen = pygame.display.set_mode((1024,screen_height))
clock = pygame.time.Clock()
running = True

PLAYER_GRAVITY = 3
y_pos = 0

collsion_list = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    player_obj = player.Rect_obj(512, 400 + y_pos, 50, 70, (180, 70, 70), screen)
    player_obj.draw()
    
    if (player_obj.y + player_obj.height) >= screen_height:
        player_obj.y = screen_height - player_obj.height
    else:
        y_pos += PLAYER_GRAVITY

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
