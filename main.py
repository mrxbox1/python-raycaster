import pygame

# initialize pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Raycaster")

# gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((255, 255, 255))

    # update the display
    pygame.display.update()

# quit
pygame.quit()
