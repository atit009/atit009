#!/usr/bin/env python3
import pygame , sys,os
pygame.init()
WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((900,500))
pygame.display.set_caption("My game")
# test_surface=pygame.Surface((200,400))
clock=pygame.time.Clock()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(25,0,0)
YELLOW=(255,255,0)
VEL=5

YELLO_HIT=pygame.USEREVENT +1
RED_HIT=pygame.USEREVENT +2

BULLTE_VEL=7
MAX_BULLETS=3
space_height,space_width=55,40
BORDER=pygame.Rect((900//2)-5,0,10,500)



Yello_space=pygame.image.load('/Users/atitsharma/Desktop/graphics/pigame/spaceship_yellow.png').convert_alpha()
Red_space=pygame.image.load('/Users/atitsharma/Desktop/graphics/pigame/spaceship_red.png').convert_alpha()
background=pygame.image.load('/Users/atitsharma/Desktop/graphics/pigame/space.png')
Yello_spaceship=pygame.transform.rotate(pygame.transform.scale(Yello_space,(space_height,space_width)),90)
red_spaceship=pygame.transform.rotate(pygame.transform.scale(Red_space,(space_height,space_width)),270)

def draw_window(red,yello,red_bullet,yellow_bullet):
    WIN.blit(background,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(Yello_spaceship,(yello.x,yello.y))
    WIN.blit(red_spaceship,(red.x,red.y))
    for bullet  in red_bullet:
        pygame.draw.rect(WIN,RED,BORDER)
    for bulet in yellow_bullet:
        pygame.draw.rect(WIN,RED,BORDER)
    pygame.display.update()

def yello_handle_movement(key_pressed,yello):
    
    if key_pressed[pygame.K_a] and yello.x -VEL> 0:
            yello.x -=VEL
    if key_pressed[pygame.K_d] and yello.x + VEL +yello.width < BORDER.x:
            yello.x +=VEL
    if key_pressed[pygame.K_s]and yello.y + VEL +yello.height<500-15:
            yello.y +=VEL
    if key_pressed[pygame.K_w]and yello.y - VEL > 0:
            yello.y -=VEL


def red_handle_movement(key_pressed,red):
    
    if key_pressed[pygame.K_LEFT] and red.x -VEL> BORDER.x + BORDER.width :
            red.x -=VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL +red.width < 900:
            red.x +=VEL
    if key_pressed[pygame.K_DOWN]and red.y + VEL +red.height<500-15:
            red.y +=VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0:
            red.y -=VEL



def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLTE_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullets in red_bullets:
        bullets.x -= BULLTE_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLO_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)




def main():

    red=pygame.Rect(700,300,space_width,space_height)
    yello=pygame.Rect(100,300,space_width,space_height)
    red_bullet=[]
    yellow_bullet=[] 
    clock=pygame.time.Clock()
    run=True
    clock.tick(60)
    while run:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                run=False
            
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_LCTRL and len(yellow_bullet)< MAX_BULLETS:
                    bullet=(yello.x + yello.width,yello.y+yello.height//2-2,10,5)
                    yellow_bullet.append(bullet)

                if events.key==pygame.K_p and len(red_bullet)< MAX_BULLETS:
                    bullet=(red.x , red.y+red.height//2-2,10,5)
                    red_bullet.append(bullet)



        
        key_pressed=pygame.key.get_pressed()
        yello_handle_movement(key_pressed,yello)
        red_handle_movement(key_pressed,red)
        handle_bullets(yellow_bullet,red_bullet,yello,red)
        draw_window(red,yello,red_bullet,yellow_bullet)
    
    pygame.quit()



if __name__=="__main__":
    main()
