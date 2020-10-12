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
    if lenght > 5:
        tree(surface,lenght*0.85,angle-math.pi/64,x + math.cos(angle)*lenght,y + math.sin(angle)*lenght,bold*0.5)
        tree(surface,lenght*0.50,angle+math.pi/2,x + math.cos(angle)*lenght,y + math.sin(angle)*lenght,bold*0.5)
        tree(surface,lenght*0.50,angle-math.pi/2,x + math.cos(angle)*lenght,y + math.sin(angle)*lenght,bold*0.5)
    
tree(screen,125,-math.pi/2,500,800,25)
pygame.display.flip()

yolo = True
while yolo:
    for event in pygame.event.get():
        if event.type == QUIT:
            yolo = False
    clock.tick(2)

pygame.quit()
