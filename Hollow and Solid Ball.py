#importing and initialising pygame
import pygame
pygame.init()

#making screen
window = pygame.display.set_mode((400, 400))
#making the screen white
window.fill((255, 255, 255))

#defying colors
Green = (250, 163, 255)

#Drawing a solid circle
pygame.draw.circle(window, Green, (300, 300), 50)

#Drawing an outlined circle
pygame.draw.circle(window, Green, (100, 100), 50, 3)

#drawing the surface object to the screen
pygame.display.update()

#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

#quit game
pygame.quit()

   #Circles for the circles  (RGB)
#   190, 227, 57   [Green]
#   255, 241, 148   [Yellow]
#   250, 163, 255   [Pink]