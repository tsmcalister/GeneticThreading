import sys, pygame, random, math
import canvas


pygame.init()

size = width, height = 900, 900
speed = [2, 2]
black = 0, 0, 0
white = 255,255,255

screen = pygame.display.set_mode(size)

gene = canvas.randomGene(100)
geneM = canvas.geneToMatrix(gene)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    gene = canvas.randomGene(100)
    geneM = canvas.geneToMatrix(gene)
    screen.fill(black)
    canvas.drawWheel(screen,geneM)
    pygame.display.flip()