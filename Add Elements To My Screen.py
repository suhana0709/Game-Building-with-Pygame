import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
color = (242, 133, 202)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, color, pygame.Rect(40, 40, 300, 300))  
    pygame.display.flip()