import pygame
from pygame.locals import QUIT
import math

pygame.init()
screen = pygame.display.set_mode((1000,800))
screen.fill((0,0,0))
clock = pygame.time.Clock()

def tree(surface,lenght,angle,x,y,bold):
    color = (0,255,0) if lenght < 30 else (136, 66, 29)
    pygame.draw.line(surface,color,(x,y),(x + math.cos(angle)*lenght,y + math.sin(angle)*lenght),math.ceil(bold))
    pygame.display.flip()
    if lenght > 15:
        tree(surface,lenght*0.8,angle-math.pi/8,x + math.cos(angle)*lenght,y + math.sin(angle)*lenght,bold*0.8)
        tree(surface,lenght*0.8,angle+math.pi/8,x + math.cos(angle)*lenght,y + math.sin(angle)*lenght,bold*0.8)   

tree(screen,150,-math.pi/2,500,800,25)
pygame.display.flip()

yolo = True
while yolo:
    for event in pygame.event.get():
        if event.type == QUIT:
            yolo = False
    clock.tick(2)

pygame.quit()
