#!/usr/bin/env python3
import pygame
from pyparsing import White
pygame.init()
WHITE=(255,255,255)
screen=pygame.display.set_mode((800,400))
a=pygame.image.load('/Users/atitsharma/Desktop/graphics/player_walk_1.png')
a_rect=a.get_rect(center=(100,200))
dis=0








while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
        if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_a and a_rect.bottom>=300:
                    dis+= -20
        
        
                
    dis+=1
    a_rect.y +=dis
    
    if a_rect.bottom >=300 : a_rect.bottom=300
    screen.fill(WHITE)         
    screen.blit(a,a_rect)
    pygame.display.update()