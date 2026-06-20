import pygame
import math
import json
import os

# some constants and shit
WIDTH = 800
HEIGHT = 600

# deltatime
dt = 0
FPS = 0

# initialize pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"python-raycaster ({FPS} FPS)")
CLOCK = pygame.time.Clock()

# set the player position and direction
player_posX = 1.5
player_posY = 1.5
player_dirX = 1
player_dirY = 0
player_moveSpeed = 0.005
player_rotSpeed = 0.0025

# set the camera plane
plane_X = 0
plane_Y = 0.66

# create the tilemap
tilemap = json.loads(open(os.getcwd() + '/tiles.json', 'r').read())

# colormap
colormap = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]

# gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    

    
    # no color in the background
    window.fill((0, 0, 0))
    


    # the magic that i don't understand begins here
    for x in range(WIDTH):
        camera_X = 2 * x / WIDTH - 1
        ray_dirX = player_dirX + plane_X * camera_X
        ray_dirY = player_dirY + plane_Y * camera_X

        player_mapX = int(player_posX)
        player_mapY = int(player_posY)

        side_distX = 0
        side_distY = 0
        
        if ray_dirX == 0: 
            _x = 1e30
        else:
            _x = ray_dirX
        if ray_dirY == 0:
            _y = 1e30
        else:
            _y = ray_dirY

        delta_distX = abs(1 / _x)
        delta_distY = abs(1 / _y)
        perp_wallDist = 0

        step_X = 0
        step_Y = 0

        hit = 0
        side = 0

        if ray_dirX < 0:
            step_X = -1
            side_distX = (player_posX - player_mapX) * delta_distX
        else:
            step_X = 1
            side_distX = (player_mapX + 1 - player_posX) * delta_distX
        if ray_dirY < 0:
            step_Y = -1
            side_distY = (player_posY - player_mapY) * delta_distY
        else:
            step_Y = 1
            side_distY = (player_mapY + 1 - player_posY) * delta_distY

        while hit == 0:
            if side_distX < side_distY:
                side_distX += delta_distX
                player_mapX += step_X
                side = 0
            else:
                side_distY += delta_distY
                player_mapY += step_Y
                side = 1
            if tilemap[player_mapY][player_mapX] > 0:
                hit = 1

        if side == 0:
            perp_wallDist = (side_distX - delta_distX)
        else:
            perp_wallDist = (side_distY - delta_distY)
        
        if perp_wallDist == 0:
            _p = 1e30
        else:
            _p = perp_wallDist
        line_height = int(HEIGHT / _p)
        
        draw_start = -line_height / 2 + HEIGHT / 2
        if draw_start < 0:
            draw_start = 0
        draw_end = line_height / 2 + HEIGHT / 2
        if draw_end >= HEIGHT:
            draw_end = HEIGHT - 1

        color = (0, 0, 0)
        if tilemap[player_mapY][player_mapX] != 0:
            color = colormap[tilemap[player_mapY][player_mapX] - 1]

        if side == 1:
            color = (color[0] / 2, color[1] / 2, color[2] / 2)

        pygame.draw.line(window, color, (x, draw_start), (x, draw_end))



    # up/down player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        #print("up")
        _s = player_moveSpeed
    elif keys[pygame.K_DOWN]:
        #print("down")
        _s = -player_moveSpeed
    else:
        _s = 0
    
    # TODO: implement a collision system that actually works
    # collision + movement, i guess
    #if tilemap[int(player_posX + player_dirX * _s * dt)][int(player_posY)] == False:
    player_posX += player_dirX * _s * dt
    #if tilemap[int(player_posX)][int(player_posY + player_dirY * _s * dt)] == False:
    player_posY += player_dirY * _s * dt
    
    # left/right player movement
    if keys[pygame.K_LEFT]:
        #print("left")
        _s = -player_rotSpeed
    elif keys[pygame.K_RIGHT]:
        #print("right")
        _s = player_rotSpeed
    else:
        _s = 0
    
    # rotation and some trigonometry that my stupid brain cannot comprehend
    old_dirX = player_dirX
    player_dirX = player_dirX * math.cos(_s * dt) - player_dirY * math.sin(_s * dt)
    player_dirY = old_dirX * math.sin(_s * dt) + player_dirY * math.cos(_s * dt)
    old_planeX = plane_X
    plane_X = plane_X * math.cos(_s * dt) - plane_Y * math.sin(_s * dt)
    plane_Y = old_planeX * math.sin(_s * dt) + plane_Y * math.cos(_s * dt)



    # update the display
    dt = CLOCK.tick()
    #print(dt)
    FPS = int(CLOCK.get_fps())
    pygame.display.set_caption(f"python-raycaster ({FPS} FPS)")
    pygame.display.update()

# quit
pygame.quit()
