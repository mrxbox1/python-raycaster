import pygame

# initialize pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Raycaster")

# set the player position (in tiles)
player_position = (1, 1)

# create the tilemap
tilemap = [[1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,1],
           [1,0,1,0,0,1,0,1],
           [1,0,1,0,0,1,0,1],
           [1,0,0,0,0,0,0,1],
           [1,0,1,1,1,1,0,1],
           [1,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1]]

# gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((0, 0, 0))

    # draw the tilemap
    for row in range(len(tilemap)):
        for tile in range(len(tilemap[row])):
            if tilemap[row][tile] != 0:
                _color = (0, 255, 0)
            else:
                _color = (64, 64, 64)
            pygame.draw.rect(window, _color, [tile*8, row*8, 8, 8])

    # update the display
    pygame.display.update()

# quit
pygame.quit()
