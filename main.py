import sys, pygame
import colors as c


pygame.init()

size = width, height = 643, 483
cell_size = 16
radius = 6
gap_size = 4

listOfCircles = []

screen = pygame.display.set_mode(size)
run = True
while run:
    screen.fill(c.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            listOfCircles.append((x, y))
            # pygame.draw.circle(screen, c.red, (x, y), radius)

    for x in range(gap_size, width, cell_size + gap_size):
        for y in range(gap_size, height, cell_size + gap_size):
            color = c.white
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
    for circle in listOfCircles:
        pygame.draw.circle(screen, c.red, circle, radius)
    pygame.display.update()