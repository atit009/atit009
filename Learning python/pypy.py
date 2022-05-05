#!/usr/bin/env python3
from trace import Trace
import  pygame
from sys import exit
def display_score():
    current_time=(pygame.time.get_ticks()//1000)-start_time
    text_surface=test_font.render(f"Score: {current_time}",False,'Black')
    score_rect=text_surface.get_rect(center=(700,50))
    screen.blit(text_surface,score_rect)

pygame.init()
game_active=True
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Atit Game")
clock=pygame.time.Clock()
sky_surface=pygame.image.load('/Users/atitsharma/Desktop/graphics/Sky.png').convert()
ground_surface=pygame.image.load('/Users/atitsharma/Desktop/graphics/ground.png').convert()
snail_surface=pygame.image.load('/Users/atitsharma/Desktop/graphics/snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(bottomright=(600,300))
player_surf=pygame.image.load('/Users/atitsharma/Desktop/graphics/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80,300))
test_font=pygame.font.Font(None,50)  #........ FOR BACKGROUND
text_surface=test_font.render('Atit Sharma',False,'Green')#........ FOR BACKGROUND
score_rect=text_surface.get_rect(center=(400,50))
player_gravity=-20
start_time=0



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity= -20


            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity= -20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                snail_rect.left=800
                start_time=pygame.time.get_ticks()//1000

            

    if game_active:            
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,'Pink',score_rect)
        screen.blit(text_surface,score_rect)
        screen.blit(player_surf,player_rect)
        snail_rect.x -=5
        if snail_rect.right<0 : snail_rect.left =800 
        screen.blit(snail_surface,snail_rect)
        display_score()

        player_gravity+=1
        player_rect.y += player_gravity
        
        if player_rect.bottom >=300 : player_rect.bottom=300
        screen.blit(player_surf,player_rect)
        if snail_rect.colliderect(player_rect):
            game_active=False

    else:
        screen.fill("Yellow")
    pygame.display.update()
    clock.tick(60)      