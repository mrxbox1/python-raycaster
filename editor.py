import pygame
import os



tilemap_width = int(input("Please specify a tilemap width: "))
tilemap_height = int(input("Please specify a tilemap height: "))
tilemap_name = input("File name to be saved to the current working directory? ")
selected_tileX = 0
selected_tileY = 0



tilemap = []

for row in range(tilemap_height):
    tilemap.append([])
    for tile in range(tilemap_width):
        tilemap[row].append(0)



pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tile map editor (int-based)")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP) and (selected_tileY != 0):
                selected_tileY -= 1
            if (event.key == pygame.K_DOWN) and (selected_tileY != tilemap_height - 1):
                selected_tileY += 1
            if (event.key == pygame.K_LEFT) and (selected_tileX != 0):
                selected_tileX -= 1
            if (event.key == pygame.K_RIGHT) and (selected_tileX != tilemap_width - 1):
                selected_tileX += 1

    window.fill((0, 0, 0))

    for row in range(tilemap_height):
        for tile in range(tilemap_width):
            if (row == selected_tileY) and (tile == selected_tileX):
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)

            pygame.draw.rect(window, color, (tile*16, row*16, 15, 15))

    pygame.display.flip()
