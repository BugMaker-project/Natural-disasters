import pygame
pygame.font.init()
def FontLoad(path:str,size:int):
    tempFont=pygame.font.Font(path,size)
    return tempFont