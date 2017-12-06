import pygame
import numpy as np
import random
import math

def randomGene(wheelSize):
    geneSize = int(wheelSize*(wheelSize-1)/2)
    return[random.getrandbits(1) for _ in range(geneSize)]

def fullyConnectedGene(wheelSize):
    geneSize = int(wheelSize*(wheelSize-1)/2)
    return[1 for _ in range(geneSize)]

def geneToMatrix(gene):
    geneLength = len(gene)
    wheelSize = int(1/2*(math.sqrt(8*len(gene)+1)+1))
    #todo optimize
    lastDrawAmount = 0
    rows = []

    for i in range(0,wheelSize):
        zeroAmount = i+1
        drawAmount = wheelSize - zeroAmount + lastDrawAmount
        
        zeroes = [0 for _ in range(zeroAmount)]
        rows.append(zeroes + gene[lastDrawAmount:drawAmount])
        lastDrawAmount = drawAmount
    return rows

def drawWheel(screen,matrix):
    npins = len(matrix)

    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h
    print(width,height)
    # coordinates on the unit square translated by (1,1) then scaled by screen width and height
    pinCoordinates = [((math.cos(x*2*math.pi/npins)+1)*width/2,(math.sin(x*2*math.pi/npins)+1)*height/2) for x in range(npins)]

    for row in range(npins):
        for column in range(npins):
            # only check top right triangle of matrix
            if(column > row):
                if(matrix[row][column] == 1):
                    pygame.draw.line(screen,(255,255,255),pinCoordinates[row],pinCoordinates[column])



#print(geneToMatrix(randomGene(10)))
#print(geneToMatrix([x for x in range(1,4951)]))