import pygame
import sys


pygame.init()


WIDTH = 800
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Animated Landscape")

clock = pygame.time.Clock()


sky_blue = (135, 206, 235)
green = (34, 139, 34)
brown = (139, 69, 19)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (100, 100, 100)
black = (0, 0, 0)
sun_color = (55, 255, 0)

car_x = -100
butterfly_speed = 2
cloud_size = 60
frame_count = 0
show_message = True


running = True
while running:
    clock.tick(60)
    frame_count += 1

    
    if frame_count < 100:
        sky_blue = (135, 206, 235)   
    elif frame_count < 200:
        sky_blue = (255, 150, 100)   
    elif frame_count < 300:
        sky_blue = (100, 100, 255)   
    elif frame_count < 400:
        sky_blue = (0, 0, 50)        
    else:
        frame_count = 0              

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(sky_blue)

    
    pygame.draw.rect(screen, green, (0, 400, WIDTH, 100))

    
    if frame_count < 300:
        pygame.draw.circle(screen, sun_color, (700, 80), 50)
    else:
        pygame.draw.circle(screen, white, (700, 80), 40)
    

    pygame.draw.rect(screen, red, (300, 250, 200, 150))
    pygame.draw.polygon(screen, brown, [(280, 250), (520, 250), (400, 150)])
    pygame.draw.rect(screen, white, (370, 320, 60, 80))
    pygame.draw.rect(screen, blue, (320, 280, 40, 40))
    pygame.draw.rect(screen, blue, (440, 280, 40, 40))

    
    pygame.draw.circle(screen, white, (150, 100), cloud_size)
    pygame.draw.circle(screen, white, (190, 90), cloud_size)
    pygame.draw.circle(screen, white, (220, 100), cloud_size)


    pygame.draw.rect(screen, grey, (car_x, 350, 100, 40))
    pygame.draw.rect(screen, blue, (car_x + 20, 330, 60, 30))
    pygame.draw.circle(screen, black, (car_x + 20, 390), 10)
    pygame.draw.circle(screen, black, (car_x + 80, 390), 10)

    
    car_x += 3
    if car_x > WIDTH:
        car_x = -120

    
    if frame_count == 60:
        sun_color = (255, 255, 0)
    elif frame_count == 120:
        sun_color = (255, 200, 0)
    elif frame_count == 180:
        sun_color = (255, 150, 0)
    elif frame_count == 240:
        sun_color = (255, 100, 0)
    elif frame_count == 300:
        sun_color = (255, 255, 0)

    
    if frame_count == 60:
        cloud_size = 70
    elif frame_count == 120:
        cloud_size = 50


    if car_x > 400:
        pygame.draw.polygon(screen, grey, [(280, 250), (520, 250), (400, 150)])


    pygame.display.flip()


pygame.quit()
