import pygame
from pygame.locals import QUIT
import math

pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((0,0,0))
clock = pygame.time.Clock()

pygame.display.flip()

yolo = True
n = 1
while yolo:
    for event in pygame.event.get():
        if event.type == QUIT:
            yolo = False
    if n < 5000:
        a = n * 137.9
        r = 7 * math.sqrt(n)
        x = r * math.cos(a) + 500
        y = r * math.sin(a) + 500
        color = (int(255%n),int(255%x),int(255%y))
        pygame.draw.circle(screen,color,(int(x),int(y)),3,0)
        pygame.display.flip()
        n += 1
    clock.tick(500)

pygame.quit()
