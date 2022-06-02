##Game Title: "Revenge Of The Fallen"
##Author: Spectronaut
##Started: 11.19.21

import pygame as pg
from sys import exit 
import json
from random import randint, choice

class Arrows(pg.sprite.Sprite):
    def __init__(self,pos,speed,screen_length):
        super().__init__()
        self.image = pg.image.load('graphics/Player/fire.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.length_x_contraint = screen_length

    def destroy_arrow(self):
        if self.rect.x <= -50 or self.rect.x >= self.length_x_contraint + 50:
            self.kill()
    
    def update(self):
        self.rect.x -= self.speed
        self.destroy_arrow()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pg.image.load('graphics/Player/image00.png').convert_alpha()
        player_walk2 = pg.image.load('graphics/Player/image01.png').convert_alpha()
        player_walk3 = pg.image.load('graphics/Player/image02.png').convert_alpha()
        player_walk4 = pg.image.load('graphics/Player/image03.png').convert_alpha()
        player_walk5 = pg.image.load('graphics/Player/image04.png').convert_alpha()
        player_walk6 = pg.image.load('graphics/Player/image05.png').convert_alpha()
        player_walk7 = pg.image.load('graphics/Player/image06.png').convert_alpha()
        player_walk8 = pg.image.load('graphics/Player/image07.png').convert_alpha()
        player_walk9 = pg.image.load('graphics/Player/image08.png').convert_alpha()
        player_walk10 = pg.image.load('graphics/Player/image09.png').convert_alpha()
        player_walk11 = pg.image.load('graphics/Player/image10.png').convert_alpha()
        player_walk12 = pg.image.load('graphics/Player/image11.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2,player_walk3,player_walk4,
                            player_walk5,player_walk6,player_walk7,player_walk8,
                            player_walk9,player_walk10,player_walk11,player_walk12]
        self.player_index = 0
        self.player_jump = pg.image.load('graphics/Player/image00.png').convert_alpha()
        self.player_slash = pg.image.load('graphics/Player/slashing/04.png').convert_alpha()
        
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        
        self.jump_sound = pg.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

        self.ready = True
        self.arrows_time = 0
        self.arrows_cooldown = 75

        self.arrows = pg.sprite.Group()     
        
    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -22
            self.jump_sound.play()

        if keys[pg.K_LEFT]:
            self.rect.x -= 8

        if keys[pg.K_RIGHT]:
            self.rect.x += 8
            
        if keys[pg.K_LCTRL] and self.ready:
            self.shoot_arrow()
            self.ready = False
            self.arrows_time = pg.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_arrow_time = pg.time.get_ticks()
            if current_arrow_time - self.arrows_time >= self.arrows_cooldown:
                self.ready = True

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        #Player bounds
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 750:
            self.rect.x = 750
            
    def animation_state(self):
        keys = pg.key.get_pressed()
        if self.rect.bottom < 300:
            self.image = self.player_jump
        elif keys[pg.K_LCTRL]:
            self.image = self.player_slash
        else:
            self.player_index += 0.3
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def player_reset(self):
        self.rect = self.image.get_rect(midbottom = (80,300))

    def shoot_arrow(self):
        self.arrows.add(Arrows(self.rect.center,-8,800))
            
    def update(self):
        if game_active:
            self.player_input()
            self.apply_gravity()
            self.animation_state()
            self.recharge()
            self.arrows.update()
        else:
            self.player_reset()

class Obstacle(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'wraith':
            #wraith
            wraith_frame0 = pg.image.load('graphics/Wraith1/0.png').convert_alpha()
            wraith_frame1 = pg.image.load('graphics/Wraith1/1.png').convert_alpha()
            wraith_frame2 = pg.image.load('graphics/Wraith1/2.png').convert_alpha()
            wraith_frame3 = pg.image.load('graphics/Wraith1/3.png').convert_alpha()
            wraith_frame4 = pg.image.load('graphics/Wraith1/4.png').convert_alpha()
            wraith_frame5 = pg.image.load('graphics/Wraith1/5.png').convert_alpha()
            wraith_frame6 = pg.image.load('graphics/Wraith1/6.png').convert_alpha()
            wraith_frame7 = pg.image.load('graphics/Wraith1/7.png').convert_alpha()
            wraith_frame8 = pg.image.load('graphics/Wraith1/8.png').convert_alpha()
            wraith_frame9 = pg.image.load('graphics/Wraith1/9.png').convert_alpha()
            wraith_frame10 = pg.image.load('graphics/Wraith1/10.png').convert_alpha()
            wraith_frame11 = pg.image.load('graphics/Wraith1/11.png').convert_alpha()
            self.frames = [wraith_frame0,wraith_frame1,wraith_frame2,wraith_frame3,wraith_frame4,
                            wraith_frame5,wraith_frame6,wraith_frame7,wraith_frame8,wraith_frame9,
                            wraith_frame10,wraith_frame11]
            y_pos = randint(0,400)
            self.enemyspeed = randint(8,10)
        elif type == 'wraith2':
            #wraith2
            wraith2_frame0 = pg.image.load('graphics/Wraith2/0.png').convert_alpha()
            wraith2_frame1 = pg.image.load('graphics/Wraith2/1.png').convert_alpha()
            wraith2_frame2 = pg.image.load('graphics/Wraith2/2.png').convert_alpha()
            wraith2_frame3 = pg.image.load('graphics/Wraith2/3.png').convert_alpha()
            wraith2_frame4 = pg.image.load('graphics/Wraith2/4.png').convert_alpha()
            wraith2_frame5 = pg.image.load('graphics/Wraith2/5.png').convert_alpha()
            wraith2_frame6 = pg.image.load('graphics/Wraith2/6.png').convert_alpha()
            wraith2_frame7 = pg.image.load('graphics/Wraith2/7.png').convert_alpha()
            wraith2_frame8 = pg.image.load('graphics/Wraith2/8.png').convert_alpha()
            wraith2_frame9 = pg.image.load('graphics/Wraith2/9.png').convert_alpha()
            wraith2_frame10 = pg.image.load('graphics/Wraith2/10.png').convert_alpha()
            wraith2_frame11 = pg.image.load('graphics/Wraith2/11.png').convert_alpha()
            self.frames = [wraith2_frame0,wraith2_frame1,wraith2_frame2,wraith2_frame3,wraith2_frame4,
                            wraith2_frame5,wraith2_frame6,wraith2_frame7,wraith2_frame8,wraith2_frame9,
                            wraith2_frame10,wraith2_frame11]
            y_pos = randint(0,400)
            self.enemyspeed = randint(5,15)
        elif type == 'wraith3':
            #Wraith3
            wraith3_frame0 = pg.image.load('graphics/Wraith3/0.png').convert_alpha()
            wraith3_frame1 = pg.image.load('graphics/Wraith3/1.png').convert_alpha()
            wraith3_frame2 = pg.image.load('graphics/Wraith3/2.png').convert_alpha()
            wraith3_frame3 = pg.image.load('graphics/Wraith3/3.png').convert_alpha()
            wraith3_frame4 = pg.image.load('graphics/Wraith3/4.png').convert_alpha()
            wraith3_frame5 = pg.image.load('graphics/Wraith3/5.png').convert_alpha()
            wraith3_frame6 = pg.image.load('graphics/Wraith3/6.png').convert_alpha()
            wraith3_frame7 = pg.image.load('graphics/Wraith3/7.png').convert_alpha()
            wraith3_frame8 = pg.image.load('graphics/Wraith3/8.png').convert_alpha()
            wraith3_frame9 = pg.image.load('graphics/Wraith3/9.png').convert_alpha()
            wraith3_frame10 = pg.image.load('graphics/Wraith3/10.png').convert_alpha()
            wraith3_frame11 = pg.image.load('graphics/Wraith3/11.png').convert_alpha()
            self.frames = [wraith3_frame0,wraith3_frame1,wraith3_frame2,wraith3_frame3,wraith3_frame4,
                            wraith3_frame5,wraith3_frame6,wraith3_frame7,wraith3_frame8,wraith3_frame9,
                            wraith3_frame10,wraith3_frame11]
            y_pos = randint(0,400)
            self.enemyspeed = randint(5,10)
        elif type == 'golem':
            #golem
            golem_frame0 = pg.image.load('graphics/Golem1/0.png').convert_alpha()
            golem_frame1 = pg.image.load('graphics/Golem1/1.png').convert_alpha()
            golem_frame2 = pg.image.load('graphics/Golem1/2.png').convert_alpha()
            golem_frame3 = pg.image.load('graphics/Golem1/3.png').convert_alpha()
            golem_frame4 = pg.image.load('graphics/Golem1/4.png').convert_alpha()
            golem_frame5 = pg.image.load('graphics/Golem1/5.png').convert_alpha()
            golem_frame6 = pg.image.load('graphics/Golem1/6.png').convert_alpha()
            golem_frame7 = pg.image.load('graphics/Golem1/7.png').convert_alpha()
            golem_frame8 = pg.image.load('graphics/Golem1/8.png').convert_alpha()
            golem_frame9 = pg.image.load('graphics/Golem1/9.png').convert_alpha()
            golem_frame10 = pg.image.load('graphics/Golem1/10.png').convert_alpha()
            golem_frame11 = pg.image.load('graphics/Golem1/11.png').convert_alpha()
            self.frames = [golem_frame0,golem_frame1,golem_frame2,golem_frame3,golem_frame4,
                            golem_frame5,golem_frame6,golem_frame7,golem_frame8,golem_frame9,
                            golem_frame10,golem_frame11]
            y_pos = 302
            self.enemyspeed = randint(1,3)
        elif type == 'golem2':
            #golem2
            golem2_frame0 = pg.image.load('graphics/Golem2/0.png').convert_alpha()
            golem2_frame1 = pg.image.load('graphics/Golem2/1.png').convert_alpha()
            golem2_frame2 = pg.image.load('graphics/Golem2/2.png').convert_alpha()
            golem2_frame3 = pg.image.load('graphics/Golem2/3.png').convert_alpha()
            golem2_frame4 = pg.image.load('graphics/Golem2/4.png').convert_alpha()
            golem2_frame5 = pg.image.load('graphics/Golem2/5.png').convert_alpha()
            golem2_frame6 = pg.image.load('graphics/Golem2/6.png').convert_alpha()
            golem2_frame7 = pg.image.load('graphics/Golem2/7.png').convert_alpha()
            golem2_frame8 = pg.image.load('graphics/Golem2/8.png').convert_alpha()
            golem2_frame9 = pg.image.load('graphics/Golem2/9.png').convert_alpha()
            golem2_frame10 = pg.image.load('graphics/Golem2/10.png').convert_alpha()
            golem2_frame11 = pg.image.load('graphics/Golem2/11.png').convert_alpha()
            golem2_frame12 = pg.image.load('graphics/Golem2/12.png').convert_alpha()
            golem2_frame13 = pg.image.load('graphics/Golem2/13.png').convert_alpha()
            golem2_frame14 = pg.image.load('graphics/Golem2/14.png').convert_alpha()
            golem2_frame15 = pg.image.load('graphics/Golem2/15.png').convert_alpha()
            golem2_frame16 = pg.image.load('graphics/Golem2/16.png').convert_alpha()
            golem2_frame17 = pg.image.load('graphics/Golem2/17.png').convert_alpha()
            golem2_frame18 = pg.image.load('graphics/Golem2/18.png').convert_alpha()
            golem2_frame19 = pg.image.load('graphics/Golem2/19.png').convert_alpha()
            golem2_frame20 = pg.image.load('graphics/Golem2/20.png').convert_alpha()
            golem2_frame21 = pg.image.load('graphics/Golem2/21.png').convert_alpha()
            golem2_frame22 = pg.image.load('graphics/Golem2/22.png').convert_alpha()
            golem2_frame23 = pg.image.load('graphics/Golem2/23.png').convert_alpha()
            self.frames = [golem2_frame0,golem2_frame1,golem2_frame2,golem2_frame3,golem2_frame4,
                            golem2_frame5,golem2_frame6,golem2_frame7,golem2_frame8,golem2_frame9,
                            golem2_frame10,golem2_frame11,golem2_frame12,golem2_frame13,golem2_frame14,
                            golem2_frame15,golem2_frame16,golem2_frame17,golem2_frame18,golem2_frame19,
                            golem2_frame20,golem2_frame21,golem2_frame22,golem2_frame23]
            y_pos = 302
            self.enemyspeed = randint(3,10)
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
        
    def animation_state(self):
        self.animation_index += 0.3
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
            
    def update(self):
        self.animation_state()
        self.rect.x -= self.enemyspeed
        self.destroy()
        self.destroyobs()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def destroyobs(self):
        if player.sprite.arrows:
            for arrows in player.sprite.arrows:
                if pg.sprite.groupcollide(player.sprite.arrows,obstacle_group,True,False):
                    self.kill()     

def display_score():
    current_time = int(pg.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, 'White')
    score_rect = score_surf.get_rect(center = (50,20))
    screen.blit(score_surf,score_rect)
    return current_time

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():
    if pg.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True   

#Gamewide variables    
pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption('Revenge Of The Fallen')
clock = pg.time.Clock()
test_font = pg.font.Font('font/Pixeltype.ttf', 25)
titles_font = pg.font.Font('font/Aligator.otf', 40)
game_active = False
start_time = 0
score = 0
level_up_score = 25
level = 1
difficulty_timer = 1800
# bg_music = pg.mixer.Sound('audio/music.wav')
# bg_music.play(loops = -1)

#Groups
player = pg.sprite.GroupSingle()
player.add(Player())

obstacle_group = pg.sprite.Group()

sky_surf = pg.image.load('graphics/skyDark.png').convert_alpha()
trees_surf = pg.image.load('graphics/BackgroundTrees.png').convert_alpha()
trees_index = 0
trees_width = 800
ground_surf = pg.image.load('graphics/boxesandcontainer.png').convert_alpha()
ground_index = 0
ground_width = 800

#player stand screen
player_stand = pg.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

#Title 
title_surf = titles_font.render('Revenge Of The Fallen', False, 'White')
title_rect = title_surf.get_rect(center = (400,50))

#start screen background
startScreen_back = pg.image.load('graphics/Start Screen.jpeg').convert_alpha()
startScreen_back_rect = player_stand.get_rect()

player_stand = pg.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

#Start Instructions
instruction_surf = test_font.render('Press Space to Start', False, 'White')
instruction_rect = title_surf.get_rect(center = (500,350))

#Timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer,difficulty_timer)

#high score data
data = {
    'HighScore': 0
}
    
try:
    with open('highscoredata.txt') as high_score_file:
        data = json.load(high_score_file)
except:
    print('No high score data found')
    
while True:
    for event in pg.event.get():   
        if event.type == pg.QUIT:
            #write the high score
            with open('highscoredata.txt','w') as high_score_file:
                json.dump(data,high_score_file)
                
            pg.quit()
            exit()
        #Restart the game  
        if game_active == False:  
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE: 
                    game_active = True
                    start_time = int(pg.time.get_ticks() / 1000)
                    high_score_indicator = False
        #Obstacle frequency using the timer         
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['golem2','wraith3','golem2','wraith','wraith2','golem2','wraith3','golem','wraith'])))

    if game_active:
        #environment elements
        screen.blit(sky_surf,(0,0))
        
        #loop the trees
        screen.blit(trees_surf, (trees_index,50))
        screen.blit(trees_surf, (trees_width + trees_index,50))
        if trees_index == -trees_width:
            screen.blit(trees_surf, (trees_index,50))
            trees_index = 0
        trees_index -= 0.25
        screen.blit(ground_surf, (ground_index,300))
        screen.blit(ground_surf, (ground_width + ground_index,300))
        if ground_index == -ground_width:
            screen.blit(ground_surf, (ground_index,300))
            ground_index = 0
            
        ground_index -= 1
        score = display_score()
        
        #player on screen
        player.draw(screen)
        player.update()
        player.sprite.arrows.draw(screen)

        #obstacles on screen
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # Collision
        game_active = collision_sprite()

        if score >= level_up_score:
            difficulty_timer = difficulty_timer - 150
            level_up_score = level_up_score + 20
            pg.time.set_timer(obstacle_timer,difficulty_timer)
            level = level + 1

        level_surf = test_font.render(f'Level: {level}', False, 'White')
        level_rect = level_surf.get_rect(center = (750,20))
        screen.blit(level_surf,level_rect) 

    else:
        #out of game menu
        screen.blit(startScreen_back,startScreen_back_rect)
        screen.blit(player_stand,player_stand_rect)
        player_gravity = 0
        #screen.blit(title_surf,title_rect)
        
        #Write the high score 
        if data["HighScore"] < score:
            data["HighScore"] = score
            high_score_indicator = True

        #restart instructions
        restart_surf = test_font.render(f'Your Score: {score}', False, 'White')
        restart_rect = restart_surf.get_rect(center = (400,350))
        
        #reset the player position - uses player_reset 
        level_up_score = 25
        difficulty_timer = 1800
        level = 1
        trees_index = 0
        player.update()
        
        if score == 0:
            screen.blit(instruction_surf,instruction_rect)
        elif high_score_indicator:
            high_score_surf = test_font.render(f'HIGH SCORE!!: {score}', False, 'Red')
            high_score_rect = high_score_surf.get_rect(midbottom = (400,350))
            screen.blit(high_score_surf,high_score_rect)
        else:
            screen.blit(restart_surf,restart_rect)

    pg.display.update()
    clock.tick(60)
    