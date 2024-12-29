import pygame
from pygame import *

screen_width = 600
screen_height = 600
squarex = 30
squarey = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("color changing square by Alp")
current_color = "white"
squarewidth = 60
squareheight = 60
run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            run = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            squarex = squarex - 25
            
        if pressed[pygame.K_RIGHT]:
            squarex = squarex + 25

        if pressed[pygame.K_DOWN]:
            squarey = squarey + 25

        if pressed[pygame.K_UP]:
            squarey = squarey - 25

        x = min(max(0,squarex), screen_width - squarewidth)
        y = min(max(0, squarey), screen_height - squareheight)



        if squarex < 10:
            current_color = "red"

        elif squarex > 500:
            current_color = "blue"

        elif squarey < 10:
            current_color = "green"

        elif squarey > 500:
            current_color = "yellow"

        else:
            current_color = "white"


        
    screen.fill("black")
    pygame.draw.rect(screen, current_color, (squarex, squarey, squarewidth, squareheight))
    pygame.display.update()
        




