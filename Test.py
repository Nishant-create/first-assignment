import pygame
from pygame.locals import *

pygame.init()

white = (255,255,255)

height = 400
width = 500

display_surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('image')

image = pygame.image.load(r'F:/Images and documents and other things/Images/download.jpg')

while True:
    display_surface.fill(white)
    display_surface.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    