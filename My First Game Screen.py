import pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
colour = (3, 252, 111)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(colour)
    pygame.display.flip()