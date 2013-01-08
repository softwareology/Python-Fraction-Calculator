import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (128, 128, 128)
YELLOW = (0, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (128, 255, 255)
WHITE = (255, 255, 255)

def showText(screen, x, y, msg, size=48, txtc=BLACK, bgc=WHITE, anti=True, font=None):
    font = pygame.font.SysFont(font, size)
    text = font.render(msg, anti, txtc, bgc)
    textRect = text.get_rect()
    textRect.left = x
    textRect.top = y
    screen.blit(text, textRect)

def drawPixel(screen, x, y, color):
    array = pygame.PixelArray(screen)
    array[x][y] = color
    del array

def drawRect(screen, x, y, w, l, color):
    pygame.draw.rect(screen, color, (x, y, w, l))
    
