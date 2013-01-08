import pygame, sys

def winInit(caption='Pygame', icon=None, winx=500, winy=500, a=0, b=0):
    pygame.init()
    pygame.display.set_caption(caption)
    icon = pygame.transform.scale(pygame.image.load(icon), (32, 32))
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((winx, winy), a, b)
    return screen

def terminate():
    pygame.quit()
    sys.exit()
