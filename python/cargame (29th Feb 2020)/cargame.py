import pygame
import time
import random
start_time=time.time()
pygame.init()
x=0
start_time=time.time()
y=0
enemy_y=-10
enemies=[]
flag=2#for lane
flagenemy=1
player_width=94#width of our car
lane_width=900/3#width of individual lane
player_y=400# y coordinate for drawing car
#clock = pygame.time.Clock()
screen_height=600
screen_width=900
screen=pygame.display.set_mode((screen_width,screen_height))
background_image=pygame.image.load("road.png").convert()
sprite_image=pygame.image.load("game_sprite.png").convert_alpha()
sprite_enemy=pygame.image.load("enemy.png").convert_alpha()

running =True

def move_background(x,y,screen_height,screen,background_image,enemy_x,player_y):
    real_y=y%screen_height


    screen.blit(background_image,(x,real_y-screen_height))
    
    if real_y<screen_height:
        screen.blit(background_image,(x,real_y))
        
    y+=1
    
    return y   

def generate_enemies(enemy_y, lane_width,enemies,car_width):
    flag = random.randint(1,3)
    enemies.append([int(flag *lane_width-(lane_width+car_width)/2),enemy_y,flag])

def enemy_moment(enemies,screen,sprite_enemy):
    if len(enemies)<=0: return
    for enemy in enemies:
        screen.blit(sprite_enemy,(enemy[0],enemy[1]))

        enemy[1]+=2

def splice_enemies(enemies):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy = enemies.index(enemy)
            enemies.pop(index_enemy)
    return enemies

#clock.tick(60)
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:#key press huda k garne bhanera define gareko 
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                if flag<=1:
                    continue
                flag-=1
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                if flag>=3:#right key has no effect on 3
                    continue
                flag+=1
        if event.type==pygame.KEYUP:#key release huda k garne bhanera define gareko 
            pass  
        player_x=int(flag*lane_width-(lane_width+player_width)/2)  
        if(time.time()-start_time>3):
            start_time=time.time()
            generate_enemies(enemy_y,lane_width,enemies,player_width)
        enemy_x=flagenemy*lane_width-(lane_width+player_width)/2
    y=move_background(x,y,screen_height,screen,background_image,enemy_x,player_y)
    

    screen.blit(sprite_image,(player_x,player_y))
    enemy_moment(enemies,screen,sprite_enemy)
    
    pygame.display.update()
    enemies=splice_enemies(enemies)
    

    #sprite--mario in mario game
    #background chai move garaune 
    #sprite sheet--