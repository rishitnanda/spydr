#pygame.mixer.music.play(-1) for bg music

import pygame
from pygame.locals import *
import random
import sys
import os
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200, 650))

icon = pygame.image.load('D:\\pygame\\SPYDR\\icon.png')

pygame.display.set_caption("SPYDR Game Hub")
pygame.display.set_icon(icon)

#fonts
score_font= pygame.font.Font('D:\\pygame\\SPYDR\\score_ping-pong.ttf', 85)
resume_clock_font= pygame.font.Font('D:\\pygame\\SPYDR\\clock_ping-pong.otf', 50)
win_font= pygame.font.Font('D:\\pygame\\SPYDR\\winner_ping-pong.ttf', 80)
input_font= pygame.font.Font('D:\\pygame\\SPYDR\\input_ping-pong.otf', 30)
gamename_font= pygame.font.Font('D:\\pygame\\SPYDR\\input_ping-pong.otf', 40)
heading_font= pygame.font.Font('D:\\pygame\\SPYDR\\heading_ping-pong.ttf',110)
banner_font= pygame.font.Font('D:\\pygame\\SPYDR\\heading_ping-pong.ttf',40)
bannerbelow_font= pygame.font.Font('D:\\pygame\\SPYDR\\heading_ping-pong.ttf',30)
pause_font= pygame.font.Font('D:\\pygame\\SPYDR\\clock_ping-pong.otf', 25)

#sounds
button_sound = pygame.mixer.Sound('D:\\pygame\\SPYDR\\button.wav')
button_sound.set_volume(1)
bounce_sound = pygame.mixer.Sound('D:\\pygame\\SPYDR\\ball_bounce.wav')
bounce_sound.set_volume(1)
tick_sound = pygame.mixer.Sound('D:\\pygame\\SPYDR\\timer.wav')
tick_sound.set_volume(1)

#image load
main_bg = pygame.image.load("D:\\pygame\\SPYDR\\bg.png")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
chess_thumb = pygame.image.load("D:\\pygame\\SPYDR\\chessthumbnail.png")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
pingpong_thumb = pygame.image.load("D:\\pygame\\SPYDR\\pingpongthumbnail.jpg")

def mainscreen():

    screen.blit(main_bg, (0, 0))
    
    heading_text = heading_font.render('S.P.Y.D.R.', True, (255, 255, 255))
    heading_rect = heading_text.get_rect()
    heading_rect.center = 600, 80
    screen.blit(heading_text, heading_rect)
    
    screen.blit(pingpong_thumb,(100,166))
    pingpong_text = gamename_font.render('Ping Pong', True, (255, 255, 255))
    pingpong_rect = pingpong_text.get_rect()
    pingpong_rect.center = 255,362
    screen.blit(pingpong_text, pingpong_rect)
    
    screen.blit(pingpong_thumb,(445,166))
    gamename_text = gamename_font.render('Ping Pong', True, (255, 255, 255))
    gamename_rect = gamename_text.get_rect()
    gamename_rect.center = 600,362
    screen.blit(gamename_text, gamename_rect)
    
    screen.blit(pingpong_thumb,(790,166))
    gamename_text = gamename_font.render('Ping Pong', True, (255, 255, 255))
    gamename_rect = gamename_text.get_rect()
    gamename_rect.center = 945,362
    screen.blit(gamename_text, gamename_rect)
    
    screen.blit(chess_thumb,(100,423))
    chess_text = gamename_font.render('Chess', True, (255, 255, 255))
    chess_rect = chess_text.get_rect()
    chess_rect.center = 255,619
    screen.blit(chess_text, chess_rect)

    screen.blit(pingpong_thumb,(445,423))
    gamename_text = gamename_font.render('Ping Pong', True, (255, 255, 255))
    gamename_rect = gamename_text.get_rect()
    gamename_rect.center = 600,619
    screen.blit(gamename_text, gamename_rect)
    
    screen.blit(pingpong_thumb,(790,423))
    gamename_text = gamename_font.render('Ping Pong', True, (255, 255, 255))
    gamename_rect = gamename_text.get_rect()
    gamename_rect.center = 945,619
    screen.blit(gamename_text, gamename_rect)

    for event in pygame.event.get():

        #cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pingpongarea = pygame.Rect(100, 206, 316, 157)
            if pingpongarea.collidepoint(event.pos) or pingpong_rect.collidepoint(event.pos):
                pp()
            chessarea = pygame.Rect(100, 384, 316, 157)
            if chessarea.collidepoint(event.pos) or chess_rect.collidepoint(event.pos):
                ch()
    
    pygame.display.flip()    

#----------------------------------------PING PONG----------------------------------------#

#image load

pi_play = pygame.image.load('D:\\pygame\\SPYDR\\pi_play.png')
pi_play = pygame.transform.scale(pi_play, (50, 50))

pi_pause = pygame.image.load('D:\\pygame\\SPYDR\\pi_pause.png')
pi_pause = pygame.transform.scale(pi_pause, (50, 50))

pi_play_pause = [pi_play, pi_pause]

pi_back = pygame.image.load('D:\\pygame\\SPYDR\\pi_back.png')
pi_back = pygame.transform.scale(pi_back, (50, 50))
    
def pp():
    #positioning of bats and ball    
    x1 = 0
    y1 = 260
    x2 = 1180
    y2 = 260
    ball_pos = [600, 325]

    #defining bat and ball speeds
    vel = 10.4
    ballvelx = 8.6
    ballvely = 8.6

    #score reset
    score1 = 0
    score2 = 0

    #direction of ball at start
    options1=[1,-1]
    answer1=random.choice(options1)
    options2=[1, -1]
    answer2=random.choice(options2)

    #variables for ease of calculation
    updownctrl=ball_pos[1]

    def pingpongscreen():
        pygame.draw.rect(screen, (255, 255, 255), (x1, y1+31.2, 20, 130))
        pygame.draw.rect(screen, (255, 255, 255), (x2, y2+31.2, 20, 130))
        pygame.draw.rect(screen, (255, 255, 255), (0, 322.5+31.2, 1300, 5))
        pygame.draw.rect(screen, (255, 255, 255), (597.5, 0+31.2, 5, 1300))
        pygame.draw.circle(screen, (255, 255, 255), (ball_pos[0], ball_pos[1]+31.2) , 15)
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1200, 60))
        pygame.draw.line(screen, (17,154,86), (142, 0), (142, 60), 6)
        pygame.draw.line(screen, (17,154,86), (1200-142, 0), (1200-142, 60), 6)
        pygame.draw.line(screen, (17,154,86), (0, 62.4), (1200, 62.4), 6)
            
        score_left_text = score_font.render(f'Score: {score1}', True, (17,154,86))
        score_left_rect = score_left_text.get_rect()
        score_left_rect.center = 68, 30
        pygame.draw.rect(screen, (255, 255, 255), (score_left_rect.topleft[0]-5, score_left_rect.topleft[1]-5, score_left_rect.width+10, score_left_rect.height+10))
        screen.blit(score_left_text, score_left_rect)
        
        score_right_text = score_font.render(f'Score: {score2}', True, (17,154,86))
        score_right_rect = score_right_text.get_rect()
        score_right_rect.center = 1200-68, 30
        pygame.draw.rect(screen, (255, 255, 255), (score_right_rect.topleft[0]-5, score_right_rect.topleft[1]-5, score_right_rect.width+10, score_right_rect.height+10))
        screen.blit(score_right_text, score_right_rect)

        global pause_rect
        global back_rect
        
        pause_rect = pygame.draw.rect(screen, (255,255,255), (570+37.5, 0, 60, 60))
        back_rect = pygame.draw.rect(screen, (255,255,255), (570-37.5, 0, 60, 60))
        
        if playcounter == 1:
            ppcount = 0
        elif playcounter == -1:
            ppcount = 1
        screen.blit(pi_play_pause[ppcount], (575+37.5, 5))
        
        screen.blit(pi_back, (575-37.5,5))
        pygame.display.flip()

    def timer():
        pingpongscreen()
              
        counter = 3
        pygame.mixer.Sound.play(tick_sound) 
        for i in range (1, 5):
            resume_clock_text = resume_clock_font.render(f' {counter} ', True, (17,154,86))
            resume_clock_rect = resume_clock_text.get_rect()
            resume_clock_rect.center = 600, 325+31.2
            pygame.draw.rect(screen, (255,255,255), resume_clock_rect)
            screen.blit(resume_clock_text, resume_clock_rect)
            
            pygame.display.update()
            pygame.time.delay(1000)        
            pygame.display.update()
            counter -= 1
        pingpongscreen()

    def wincheck():
        if score1 == m:
            while True:
                pygame.draw.rect(screen, (0, 255, 0), (0, 0, 1400, 800))
                win_text = win_font.render(f'{playerleft_input} Won!', True, (255, 255, 255))
                win_rect = win_text.get_rect()
                win_rect.center = 600, 325
                screen.blit(win_text, win_rect)
                pygame.display.update()
                
        if score2 == m:
            while True:
                pygame.draw.rect(screen, (0, 255, 0), (0, 0, 1400, 800))
                win_text = win_font.render(f'{playerright_input} Won!', True, (255, 255, 255))
                win_rect = win_text.get_rect()
                win_rect.center = 600, 325
                screen.blit(win_text, win_rect)
                pygame.display.update()


    
    #loop variables
    active_left = False
    active_right = False
    active_dmin = False
    active_dmax = False
    coninv = None
    pingpong_input = True

    #variables
    playerleft_input = ''
    playerright_input = ''
    minduce_input = ''
    maxduce_input = ''

    #input screen
    while pingpong_input:    
        screen.fill((0, 255, 0))
        heading_text = heading_font.render('Ping - Pong', True, (255, 255, 255))
        heading_rect = heading_text.get_rect()
        heading_rect.center = 600, 100
        screen.blit(heading_text, heading_rect)
        
        for event in pygame.event.get():

            #cross button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #text boxes and continue button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerleft_base.collidepoint(event.pos):
                    pygame.mixer.Sound.play(button_sound) 
                    active_left = True
                    active_right = False
                    active_dmin = False
                    active_dmax = False
                elif playerright_base.collidepoint(event.pos):
                    pygame.mixer.Sound.play(button_sound) 
                    active_right = True
                    active_left = False
                    active_dmin = False
                    active_dmax = False
                elif minduce_base.collidepoint(event.pos):
                    pygame.mixer.Sound.play(button_sound) 
                    active_dmin = True
                    active_left = False
                    active_right = False
                    active_dmax = False
                elif maxduce_base.collidepoint(event.pos):
                    pygame.mixer.Sound.play(button_sound) 
                    active_dmax = True
                    active_left = False
                    active_right = False
                    active_dmin = False
                elif continue_base.collidepoint(event.pos) and coninv=='Play!':
                    pygame.mixer.Sound.play(button_sound) 
                    active_dmax = False
                    active_left = False
                    active_right = False
                    active_dmin = False
                    pingpong_input = False
                    pingpong_run = True
                else:
                    active_dmax = False
                    active_left = False
                    active_right = False
                    active_dmin = False

            #feeding input        
            if event.type == pygame.KEYDOWN and active_left == True:
                if event.key == pygame.K_BACKSPACE:
                    playerleft_input = playerleft_input[:-1]
                elif len(playerleft_input)>20:
                    playerleft_input = playerleft_input[:-1]
                else:
                    playerleft_input += event.unicode
            elif event.type == pygame.KEYDOWN and active_right == True:
                if event.key == pygame.K_BACKSPACE:
                    playerright_input = playerright_input[:-1]
                elif len(playerright_input)>20:
                    playerright_input = playerright_input[:-1]
                else:
                    playerright_input += event.unicode
            elif event.type == pygame.KEYDOWN and active_dmin == True:
                if event.key == pygame.K_BACKSPACE:
                    minduce_input = minduce_input[:-1]
                elif len(minduce_input)>1:
                    minduce_input = minduce_input[:-1]
                else:
                    minduce_input += event.unicode
            elif event.type == pygame.KEYDOWN and active_dmax == True:
                if event.key == pygame.K_BACKSPACE:
                    maxduce_input = maxduce_input[:-1]
                elif len(maxduce_input)>1:
                    maxduce_input = maxduce_input[:-1]
                else:
                    maxduce_input += event.unicode

            #continue button customization
            if len(playerleft_input)>0 and len(playerright_input)>0 and len(minduce_input)>0 and len(maxduce_input)>0:
                if minduce_input.isnumeric() and maxduce_input.isnumeric() and 29 >= int(minduce_input) >= 0 and 40 >= int(maxduce_input) >= 2 and int(minduce_input)+2<=int(maxduce_input):
                    coninv = "Play!"
                else:
                    coninv = "Invalid Data!"
            else:
                coninv = "Incomplete Data!"

        #left player input            
        playerleft_text = input_font.render(playerleft_input, True, (0, 255, 0))
        playerleft_rect = playerleft_text.get_rect()
        playerleft_rect.topleft = 598, 219
        playerleft_base = playerleft_text.get_rect()
        playerleft_base = pygame.draw.rect(screen, (255, 255, 255), (playerleft_rect.x-10, playerleft_rect.y-10, playerleft_rect.w+20, playerleft_rect.h+20))
        pygame.draw.rect(screen, (255, 255, 255), playerleft_rect)
        screen.blit(playerleft_text, playerleft_rect)
        
        playerleft_question_text = input_font.render('Name of Player 1 (Left):', True, (255, 255, 255))
        playerleft_question_rect = playerleft_question_text.get_rect()
        playerleft_question_rect.topright = 558, 219
        screen.blit(playerleft_question_text, playerleft_question_rect)


        #right player input
        playerright_text = input_font.render(playerright_input, True, (0, 255, 0))
        playerright_rect = playerright_text.get_rect()
        playerright_rect.topleft = 598, 239+((112-4*playerleft_rect.h)/3)+playerleft_rect.h+32
        playerright_base = playerright_text.get_rect()
        playerright_base = pygame.draw.rect(screen, (255, 255, 255), (playerright_rect.x-10, playerright_rect.y-10, playerright_rect.w+20, playerright_rect.h+20))
        pygame.draw.rect(screen, (255, 255, 255), playerright_rect)
        screen.blit(playerright_text, playerright_rect)

        playerright_question_text = input_font.render('Name of Player 2 (Right):', True, (255, 255, 255))
        playerright_question_rect = playerright_question_text.get_rect()
        playerright_question_rect.topright = 558, 239+((112-4*playerleft_rect.h)/3)+playerleft_rect.h+32
        screen.blit(playerright_question_text, playerright_question_rect)
        

        #minimum duce value input
        minduce_text = input_font.render(minduce_input, True, (0, 255, 0))
        minduce_rect = minduce_text.get_rect()
        minduce_rect.topleft = 598, 259+(2*(112-4*playerleft_rect.h)/3)+2*playerleft_rect.h+64
        minduce_base = minduce_text.get_rect()
        minduce_base = pygame.draw.rect(screen, (255, 255, 255), (minduce_rect.x-10, minduce_rect.y-10, minduce_rect.w+20, minduce_rect.h+20))
        pygame.draw.rect(screen, (255, 255, 255), minduce_rect)
        screen.blit(minduce_text, minduce_rect)

        minduce_question_text = input_font.render('Minimum duce at:', True, (255, 255, 255))
        minduce_question_rect = minduce_question_text.get_rect()
        minduce_question_rect.topright = 558, 259+(2*(112-4*playerleft_rect.h)/3)+2*playerleft_rect.h+64
        screen.blit(minduce_question_text, minduce_question_rect)
        

        #maximum duce value input
        maxduce_text = input_font.render(maxduce_input, True, (0, 255, 0))
        maxduce_rect = maxduce_text.get_rect()
        maxduce_rect.topleft = 598, 279+(112-4*playerleft_rect.h)+3*playerleft_rect.h+96
        maxduce_base = maxduce_text.get_rect()
        maxduce_base = pygame.draw.rect(screen, (255, 255, 255), (maxduce_rect.x-10, maxduce_rect.y-10, maxduce_rect.w+20, maxduce_rect.h+20))
        pygame.draw.rect(screen, (255, 255, 255), maxduce_rect)
        screen.blit(maxduce_text, maxduce_rect)

        maxduce_question_text = input_font.render('Maximum duce at:', True, (255, 255, 255))
        maxduce_question_rect = maxduce_question_text.get_rect()
        maxduce_question_rect.topright = 558, 279+(112-4*playerleft_rect.h)+3*playerleft_rect.h+96
        screen.blit(maxduce_question_text, maxduce_question_rect)
        

        #continue button
        continue_text = input_font.render(f'{coninv}', True, (0, 255, 0))
        continue_rect = continue_text.get_rect()
        continue_rect.center = 600, 279+(112-4*playerleft_rect.h)+3*playerleft_rect.h+192.5
        continue_base = pygame.draw.rect(screen, (255, 255, 255), (350, 279+(112-4*playerleft_rect.h)+3*playerleft_rect.h+170, 500 , 45))
        screen.blit(continue_text, continue_rect)
        
        pygame.display.flip()

    #variables
    if pingpong_run == True:
        x=0
        speedcount=0
        k=82
        minduce_input=int(minduce_input)
        maxduce_input=int(maxduce_input)
        m=minduce_input+1
        n=maxduce_input+1
        global playcounter
        playcounter = -1
        pause=False
        
    while pingpong_run:
        bg = pygame.image.load("D:\\pygame\\SPYDR\\pingpong_bg.png")
        screen.blit(bg, (0, 0))
        if x==0:
            timer()
            shuffle = random.randint(-350,350) #change in ball direction
            shuffle=shuffle/100
            x+=1
            ballvelx += shuffle
            ballvely = (k-(ballvelx)**2)**0.5
            if ballvelx or ballvely > 0.82*k:
                ballvelx=k**0.5
                ballvely=k**0.5

        pygame.time.delay(9)
        speedcount+=1
        if speedcount==60:
            speedcount=0
            k+=1

        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_rect.collidepoint(event.pos):
                    playcounter = 1
                    pause = True
                    pingpongscreen()
                if back_rect.collidepoint(event.pos):
                    pingpong_run = False
                    back = True
                    
        while pause:
            for event2 in pygame.event.get():
                if event2.type == pygame.MOUSEBUTTONDOWN:
                    if pause_rect.collidepoint(event.pos):
                        playcounter = -1
                        pause = False
                        pingpongscreen()
              
        pygame.event.get()

        #duce configuration
        if (minduce_input+1)%2==0:
            if (score1 >= score2 and score1 == (minduce_input+1)/2) or (score2 >= score1 and score2 == (minduce_input+1)/2):
                vel += 0.015
        elif (minduce_input+1)%2!=0:
            if (score1 >= score2 and score1 == (minduce_input+2)/2) or (score2 >= score1 and score2 == (minduce_input+2)/2):
                vel += 0.015

        if score1 == m-1 == score2 and m!=n:
            m += 1

        #ball movement        
        ball_pos[0]+=answer1*ballvelx
        updownctrl+=answer2*ballvely

        #ball strikes left
        if (answer1==-1 and ball_pos[0]<=35):
            shuffle = random.randint(-350,350)
            shuffle=shuffle/100
            ballvelx += shuffle
            ballvely = (k-(ballvelx)**2)**0.5
            if ballvelx or ballvely > 0.82*k:
                ballvelx=k**0.5
                ballvely=k**0.5
            if y1-22<=ball_pos[1]<=y1+152:
              pygame.mixer.Sound.play(bounce_sound) 
              answer1 *= -1
            else:
              for i in range (1,8):
                pygame.time.delay(20)
                pygame.event.get()
                ball_pos[0]+=answer1*ballvelx
                ball_pos[1]+=answer2*ballvely
                pingpongscreen()
              ball_pos = [1300, 650]
              x1 = 0
              y1 = 260
              x2 = 1180
              y2 = 260
              score2 += 1
              bg = pygame.image.load("D:\\pygame\\SPYDR\\pingpong_bg.png")
              screen.blit(bg, (0, 0))
              pingpongscreen()
              wincheck()
              answer1 = -1
              timer()
              ball_pos = [600, 325]
              updownctrl=ball_pos[1]
              
        #ball strikes right      
        elif (answer1==1 and ball_pos[0]>=1165):
            shuffle = random.randint(-350,350) #change in ball direction
            shuffle=shuffle/100
            ballvelx += shuffle
            ballvely = (k-(ballvelx)**2)**0.5
            if ballvelx or ballvely > 0.82*k:
                ballvelx=k**0.5
                ballvely=k**0.5
            if y2-22<=ball_pos[1]<=y2+152:
              pygame.mixer.Sound.play(bounce_sound) 
              answer1 *= -1
            else:
              for i in range (1,8):
                pygame.time.delay(20)
                pygame.event.get()
                ball_pos[0]+=answer1*ballvelx
                ball_pos[1]+=answer2*ballvely
                pingpongscreen()
              ball_pos = [1300, 650]
              x1 = 0
              y1 = 260
              x2 = 1180
              y2 = 260
              score1 += 1
              bg = pygame.image.load("D:\\pygame\\SPYDR\\pingpong_bg.png")
              screen.blit(bg, (0, 0))
              pingpongscreen()
              wincheck()          
              answer1 = 1
              timer()
              ball_pos = [600, 325]
              updownctrl=ball_pos[1]          

        #ball goes up or down      
        if (answer2==-1 and updownctrl>15+62.4) or (answer2==1 and updownctrl<620):
            ball_pos[1] = updownctrl
        else:
            answer2 *= -1
            pygame.mixer.Sound.play(bounce_sound) 
            shuffle = random.randint(-350,350) #change in ball direction
            shuffle=shuffle/100
            ballvelx += shuffle
            ballvely = (k-(ballvelx)**2)**0.5
            if ballvelx or ballvely > 0.82*k:
                ballvelx=k**0.5
                ballvely=k**0.5
        #controlling bats
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT]:
            if y1-vel>0:
              y1 -= vel

        if keys[pygame.K_LCTRL]:
            if y1+vel<520:
              y1 += vel
        
        if keys[pygame.K_BACKSLASH]:
            if y2-vel>0:
              y2 -= vel
        
        if keys[pygame.K_RSHIFT]:
            if y2+vel<520:
              y2 += vel

        pingpongscreen()

#----------------------------------------PING PONG----------------------------------------#

#------------------------------------------CHESS------------------------------------------#

color1 = (242, 175, 87)
color2 = (171, 50, 26)
color3 = 1
bg1 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_1.png")
bg2 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_2.png")
bg3 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_3.png")
bg4 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_4.png")
bg5 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_5.png")
bg6 = pygame.image.load("D:\\pygame\\SPYDR\\ch_bg_6.png")
bg = [bg1, bg2, bg3, bg4, bg5, bg6]
banner = pygame.image.load('D:\\pygame\\SPYDR\\banner.png')
    
def ch():
    global winner
    global white_unkillable
    global black_unkillable
    global check
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    medium_font = pygame.font.Font('freesansbold.ttf', 40)
    big_font = pygame.font.Font('freesansbold.ttf', 50)

    timer = pygame.time.Clock()

    #game variables
    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

    captured_pieces_white = []
    captured_pieces_black = []


    # 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
    turn_step = 0
    selection = 100
    valid_moves = []
    white_unkillable = []
    black_unkillable = []
    check = False

    #game images
    black_queen = pygame.image.load('D:\\pygame\\SPYDR\\black queen.png')
    black_queen = pygame.transform.scale(black_queen, (45, 45))
    black_queen_small = pygame.transform.scale(black_queen, (20, 20))
    black_king = pygame.image.load('D:\\pygame\\SPYDR\\black king.png')
    black_king = pygame.transform.scale(black_king, (45, 45))
    black_king_small = pygame.transform.scale(black_king, (20, 20))
    black_rook = pygame.image.load('D:\\pygame\\SPYDR\\black rook.png')
    black_rook = pygame.transform.scale(black_rook, (45, 45))
    black_rook_small = pygame.transform.scale(black_rook, (20, 20))
    black_bishop = pygame.image.load('D:\\pygame\\SPYDR\\black bishop.png')
    black_bishop = pygame.transform.scale(black_bishop, (45, 45))
    black_bishop_small = pygame.transform.scale(black_bishop, (20, 20))
    black_knight = pygame.image.load('D:\\pygame\\SPYDR\\black knight.png')
    black_knight = pygame.transform.scale(black_knight, (45, 45))
    black_knight_small = pygame.transform.scale(black_knight, (20, 20))
    black_pawn = pygame.image.load('D:\\pygame\\SPYDR\\black pawn.png')
    black_pawn = pygame.transform.scale(black_pawn, (45, 45))
    black_pawn_small = pygame.transform.scale(black_pawn, (20, 20))
    white_queen = pygame.image.load('D:\\pygame\\SPYDR\\white queen.png')
    white_queen = pygame.transform.scale(white_queen, (45, 45))
    white_queen_small = pygame.transform.scale(white_queen, (20, 20))
    white_king = pygame.image.load('D:\\pygame\\SPYDR\\white king.png')
    white_king = pygame.transform.scale(white_king, (45, 45))
    white_king_small = pygame.transform.scale(white_king, (20, 20))
    white_rook = pygame.image.load('D:\\pygame\\SPYDR\\white rook.png')
    white_rook = pygame.transform.scale(white_rook, (45, 45))
    white_rook_small = pygame.transform.scale(white_rook, (20, 20))
    white_bishop = pygame.image.load('D:\\pygame\\SPYDR\\white bishop.png')
    white_bishop = pygame.transform.scale(white_bishop, (45, 45))
    white_bishop_small = pygame.transform.scale(white_bishop, (20, 20))
    white_knight = pygame.image.load('D:\\pygame\\SPYDR\\white knight.png')
    white_knight = pygame.transform.scale(white_knight, (45, 45))
    white_knight_small = pygame.transform.scale(white_knight, (20, 20))
    white_pawn = pygame.image.load('D:\\pygame\\SPYDR\\white pawn.png')
    white_pawn = pygame.transform.scale(white_pawn, (45, 45))
    white_pawn_small = pygame.transform.scale(white_pawn, (20, 20))

    white_images = [white_pawn, white_queen, white_king,
                    white_knight, white_rook, white_bishop]
    small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                          white_rook_small, white_bishop_small]

    black_images = [black_pawn, black_queen, black_king,
                    black_knight, black_rook, black_bishop]
    small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                          black_rook_small, black_bishop_small]

    piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

    # check variables/ flashing counter
    winner = ''
    game_over = False

    # draw menu
    def draw_menu():
        pygame.draw.rect(screen, 'black', [0, 0, 280, 650])
        screen.blit(banner, (0,0))
        banner_text = banner_font.render('SPYDR', True, (255, 255, 255))
        banner_rect = banner_text.get_rect()
        banner_rect.center = 140, 60
        screen.blit(banner_text, banner_rect)
        banner_text = bannerbelow_font.render('CHESS', True, (255, 255, 255))
        banner_rect = banner_text.get_rect()
        banner_rect.center = 140, 90
        screen.blit(banner_text, banner_rect)

        pygame.draw.rect(screen, (242, 175, 87), [60, 300, 30, 30])
        pygame.draw.rect(screen, (171, 50, 26), [90, 300, 30, 30])
        pygame.draw.rect(screen, (242, 175, 87), [90, 330, 30, 30])
        pygame.draw.rect(screen, (171, 50, 26), [60, 330, 30, 30])

        pygame.draw.rect(screen, (125, 240, 150), [160, 300, 30, 30])
        pygame.draw.rect(screen, (19,117,40), [190, 300, 30, 30])
        pygame.draw.rect(screen, (125, 240, 150), [190, 330, 30, 30])
        pygame.draw.rect(screen, (19,117,40), [160, 330, 30, 30])

        pygame.draw.rect(screen, (161, 171, 240), [60, 400, 30, 30])
        pygame.draw.rect(screen, (87, 107, 235), [90, 400, 30, 30])
        pygame.draw.rect(screen, (161, 171, 240), [90, 430, 30, 30])
        pygame.draw.rect(screen, (87, 107, 235), [60, 430, 30, 30])

        pygame.draw.rect(screen, (247, 184, 37), [160, 400, 30, 30])
        pygame.draw.rect(screen, (33, 33, 31), [190, 400, 30, 30])
        pygame.draw.rect(screen, (247, 184, 37), [190, 430, 30, 30])
        pygame.draw.rect(screen, (33, 33, 31), [160, 430, 30, 30])

        pygame.draw.rect(screen, (230, 235, 96), [60, 500, 30, 30])
        pygame.draw.rect(screen, (165, 96, 235), [90, 500, 30, 30])
        pygame.draw.rect(screen, (230, 235, 96), [90, 530, 30, 30])
        pygame.draw.rect(screen, (165, 96, 235), [60, 530, 30, 30])

        pygame.draw.rect(screen, (245, 211, 221), [160, 500, 30, 30])
        pygame.draw.rect(screen, (222, 53, 98), [190, 500, 30, 30])
        pygame.draw.rect(screen, (245, 211, 221), [190, 530, 30, 30])
        pygame.draw.rect(screen, (222, 53, 98), [160, 530, 30, 30])
        
        global color1
        global color2
        global color3
        area1 = pygame.Rect(60,300, 60, 60)
        area2 = pygame.Rect(160,300, 60, 60)
        area3 = pygame.Rect(60,400, 60, 60)
        area4 = pygame.Rect(160,400, 60, 60)
        area5 = pygame.Rect(60,500, 60, 60)
        area6 = pygame.Rect(160,500, 60, 60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:            
                if area1.collidepoint(event.pos):
                    color1 = (242, 175, 87)
                    color2 = (171, 50, 26)
                    color3 = 1
                    
                if area2.collidepoint(event.pos):
                    color1 = (125, 240, 150)
                    color2 = (19,117,40)
                    color3 = 2
                if area3.collidepoint(event.pos):
                    color1 = (161, 171, 240)
                    color2 = (87, 107, 235)
                    color3 = 3
                if area4.collidepoint(event.pos):
                    color1 = (247, 184, 37)
                    color2 = (0, 0, 0)
                    color3 = 4
                if area5.collidepoint(event.pos):
                    color1 = (230, 235, 96)
                    color2 = (165, 96, 235)
                    color3 = 5
                if area6.collidepoint(event.pos):
                    color1 = (245, 211, 221)
                    color2 = (222, 53, 98)
                    color3 = 6
        
    # draw main game board
    def draw_board():
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(screen, color1, [
                                 390 - (column * 130)+340, 65 + row * 65, 65, 65])
                pygame.draw.rect(screen, color2, [
                                 390 - (column * 130)+340+65, 65 + row * 65, 65, 65])
            else:
                pygame.draw.rect(screen, color1, [
                                 455 - (column * 130)+340, 65 + row * 65, 65, 65])
                pygame.draw.rect(screen, color2, [
                                 455 - (column * 130)+340-65, 65 + row * 65, 65, 65])
            pygame.draw.rect(screen, 'gold', [520+340, 0+65, 130, 520], 5)
            for i in range(9):
                pygame.draw.line(screen, 'black', (0+340, 65 * i+65), (520+340, 65 * i+65), 2)
                pygame.draw.line(screen, 'black', (65 * i+340, 0+65), (65 * i+340, 520+65), 2)


    # draw pieces onto board
    def draw_pieces():
        for i in range(len(white_pieces)):
            index = piece_list.index(white_pieces[i])
            if white_pieces[i] == 'pawn':
                screen.blit(
                    white_pawn, (white_locations[i][0] * 65 +14.3+340, white_locations[i][1] * 65 +19.5+65))
            else:
                screen.blit(white_images[index], (white_locations[i]
                            [0] * 65 + 10+340, white_locations[i][1] * 65 + 10+65))
            if turn_step < 2:
                if selection == i:
                    pygame.draw.rect(screen, 'red', [white_locations[i][0] * 65 + 1+340, white_locations[i][1] * 65 + 1+65,
                                                     65, 65], 2)

        for i in range(len(black_pieces)):
            index = piece_list.index(black_pieces[i])
            if black_pieces[i] == 'pawn':
                screen.blit(
                    black_pawn, (black_locations[i][0] * 65 +14.3+340, black_locations[i][1] * 65 +19.5+65))
            else:
                screen.blit(black_images[index], (black_locations[i]
                            [0] * 65 + 10+340, black_locations[i][1] * 65 + 10+65))
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 65 + 1+340, black_locations[i][1] * 65 + 1+65,
                                                      65, 65], 2)


    # function to check all pieces valid options on board
    def check_options(pieces, locations, turn):
        global check
        moves_list = []
        all_moves_list = []
        for i in range((len(pieces))):
            location = locations[i]
            piece = pieces[i]
            if piece == 'pawn':
                moves_list = check_pawn(location, turn)
            elif piece == 'rook':
                moves_list = check_rook(location, turn)
            elif piece == 'knight':
                moves_list = check_knight(location, turn)
            elif piece == 'bishop':
                moves_list = check_bishop(location, turn)
            elif piece == 'queen':
                moves_list = check_queen(location, turn)
            elif piece == 'king' and check == False:
                moves_list = check_king(location, turn)
            all_moves_list.append(moves_list)
        return all_moves_list


    # check king valid moves
    def check_king(position, color):
        global white_unkillable
        global black_unkillable
        global king_target
        global king_targets
        global king_moves_list
        global check
        global colour
        colour = color
        king_moves_list = []
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations       
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
        else:
            friends_list = black_locations
            enemies_list = white_locations       
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            
        # 8 squares to check for kings, they can go one square any direction
        king_targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
                   (-1, 1), (-1, -1), (0, 1), (0, -1)]
        for i in king_targets[0:8]:
            king_target = (position[0] + i[0], position[1] + i[1])
            if color == 'white' and king_target not in black_unkillable:
                white_unkillable.append(king_target)
            elif color == 'black' and king_target not in white_unkillable:
                black_unkillable.append(king_target)
            if king_target not in friends_list and 0 <= king_target[0] <= 7 and 0 <= king_target[1] <= 7:
                if color == 'white':
                    if king_target not in black_unkillable:
                        king_targets.append(king_target)
                        king_moves_list.append(king_target)
                if color == 'black':
                    if king_target not in white_unkillable:
                        king_targets.append(king_target)
                        king_moves_list.append(king_target)
                draw_check()
                check = False
        return king_moves_list


    # check queen valid moves
    def check_queen(position, color):
        global white_unkillable
        global black_unkillable
        moves_list = check_bishop(position, color)
        second_list = check_rook(position, color)
        for i in range(len(second_list)):
            moves_list.append(second_list[i])
        return moves_list


    # check bishop moves
    def check_bishop(position, color):
        global white_unkillable
        global black_unkillable
        moves_list = []
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
        for i in range(4):  # up-right, up-left, down-right, down-left
            path = True
            chain = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            else:
                x = -1
                y = 1
            while path:
                if color == 'white':
                    white_unkillable.append((position[0] + (chain * x), position[1] + (chain * y)))
                elif color == 'black':
                    black_unkillable.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                        0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append(
                        (position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list


    # check rook moves
    def check_rook(position, color):
        global white_unkillable
        global black_unkillable
        moves_list = []
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
        for i in range(4):  # down, up, right, left
            path = True
            chain = 1
            if i == 0:
                x = 0
                y = 1
            elif i == 1:
                x = 0
                y = -1
            elif i == 2:
                x = 1
                y = 0
            else:
                x = -1
                y = 0
            while path:
                if color == 'white':
                    white_unkillable.append((position[0] + (chain * x), position[1] + (chain * y)))
                elif color == 'black':
                    black_unkillable.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                        0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                    moves_list.append(
                        (position[0] + (chain * x), position[1] + (chain * y)))
                    if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                        path = False
                    chain += 1
                else:
                    path = False
        return moves_list


    # check valid pawn moves
    def check_pawn(position, color):
        global white_unkillable
        global black_unkillable
        moves_list = []
        if color == 'white':
            white_unkillable.append((position[0] - 1, position[1] + 1))
            white_unkillable.append((position[0] + 1, position[1] + 1))
            if (position[0], position[1] + 1) not in white_locations and \
                    (position[0], position[1] + 1) not in black_locations and position[1] < 7:
                moves_list.append((position[0], position[1] + 1))
            if (position[0], position[1] + 2) not in white_locations and \
                    (position[0], position[1] + 2) not in black_locations and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
            if (position[0] + 1, position[1] + 1) in black_locations:
                moves_list.append((position[0] + 1, position[1] + 1))
            if (position[0] - 1, position[1] + 1) in black_locations:
                moves_list.append((position[0] - 1, position[1] + 1))      
        else:
            black_unkillable.append((position[0] + 1, position[1] - 1))
            black_unkillable.append((position[0] - 1, position[1] - 1)) 
            if (position[0], position[1] - 1) not in white_locations and \
                    (position[0], position[1] - 1) not in black_locations and position[1] > 0:
                moves_list.append((position[0], position[1] - 1))
            if (position[0], position[1] - 2) not in white_locations and \
                    (position[0], position[1] - 2) not in black_locations and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
            if (position[0] + 1, position[1] - 1) in white_locations:
                moves_list.append((position[0] + 1, position[1] - 1))
            if (position[0] - 1, position[1] - 1) in white_locations:  
                moves_list.append((position[0] - 1, position[1] - 1))               
        return moves_list


    # check valid knight moves
    def check_knight(position, color):
        global white_unkillable
        global black_unkillable
        moves_list = []
        if color == 'white':
            enemies_list = black_locations
            friends_list = white_locations
        else:
            friends_list = black_locations
            enemies_list = white_locations
        # 8 squares to check for knights, they can go two squares in one direction and one in another
        targets = [(1, 2), (1, -2), (2, 1), (2, -1),
                   (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            if color == 'white':
                white_unkillable.append(target)
            elif color == 'black':
                black_unkillable.append(target)
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)
        return moves_list


    # check for valid moves for just selected piece
    def check_valid_moves():
        if turn_step < 2:
            options_list = white_options
        else:
            options_list = black_options
        valid_options = options_list[selection]
        return valid_options


    # draw valid moves on screen
    def draw_valid(moves):
        if turn_step < 2:
            color = 'red'
        else:
            color = 'blue'
        for i in range(len(moves)):
            pygame.draw.circle(
                screen, color, (moves[i][0] * 65 + 340+32.5, moves[i][1] * 65 + 65+32.5), 5)


    # draw captured pieces on side of screen
    def draw_captured():
        for i in range(len(captured_pieces_white)):
            captured_piece = captured_pieces_white[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_black_images[index], (536.25+340, 5 + 32.5 * i+65))
        for i in range(len(captured_pieces_black)):
            captured_piece = captured_pieces_black[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_white_images[index], (601.25+340, 5 + 32.5 * i+65))


    # draw a flashing square around king if in check
    def draw_check():
        global winner
        global king_target
        global king_targets
        global king_moves_list
        global check
        check = True
        black_checkers = []
        white_checkers = []
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        black_king_index = black_pieces.index('king')
        black_king_location = black_locations[black_king_index]
        white_king_index = white_pieces.index('king')
        white_king_location = white_locations[white_king_index]
        
        if king_targets[0:8]== [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]:
            king_targets = king_targets[8:]
        if colour == 'white':
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 65 + 1 +340,
                                                          white_locations[king_index][1] * 65 + 1 +65, 65, 65], 5)
                    
                for k in range(len(king_targets)-1, -1, -1):
                    king_target = king_targets[k]
                    
                    for o in black_options:
                        if king_target in o and king_target in king_targets:
                            king_targets.remove(king_target)
                            king_moves_list.remove(king_target)
                if king_targets == []:
                    checkers()
                            
        elif colour == 'black':
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]

            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 65 + 1 +340,
                                                          black_locations[king_index][1] * 65 + 1 +65, 65, 65], 5)
                    
                for k in range(len(king_targets)-1, -1, -1):
                    king_target = king_targets[k]
                                        
                    for o in white_options:
                        if king_target in o and king_target in king_targets:
                            king_targets.remove(king_target)
                            king_moves_list.remove(king_target)
                if king_targets == []:
                    checkers()


    def draw_game_over():
        pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
        screen.blit(font.render(
            f'{winner} won the game!', True, 'white'), (210, 210))
        screen.blit(font.render(f'Press ENTER to Restart!',
                    True, 'white'), (210, 240))

    def checkers():
        global winner
        global colour
        lose = False
        black_checkers = []
        white_checkers = []
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        black_king_index = black_pieces.index('king')
        black_king_location = black_locations[black_king_index]
        white_king_index = white_pieces.index('king')
        white_king_location = white_locations[white_king_index]

        if colour == 'black':
            for i in white_options:
                if black_king_location in i:
                    white_checkers.append(white_locations[white_options.index(i)])
                    for j in white_checkers:
                        for k in black_options:
                            if j in k:
                                lose = False
            if lose == True:
                winner = 'white'                              
                    
        if colour == 'white':
            for i in black_options:
                if white_king_location in i:
                    black_checkers.append(black_locations[black_options.index(i)])
                    lose = True
                    for j in black_checkers:
                        for k in white_options:
                            if j in k:
                                lose = False
            if lose == True:
                winner = 'black'

    def protect_king():
        global white_options
        global black_options
        black_checkers = []
        white_checkers = []
        if colour == 'white':
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):            
                if king_location in black_options[i]:
                    for s in black_options:
                        if king_location in s:
                            black_checkers.append(black_locations[black_options.index(s)])
                    for q in range(0, len(white_options)):
                        store = white_options[white_pieces.index('king')]
                        white_options[q] = [r for r in white_options[q] if r in black_checkers]
                        white_options[white_pieces.index('king')] = store
        if colour == 'black':
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):            
                if king_location in white_options[i]:
                    for s in white_options:
                        if king_location in s:
                            white_checkers.append(white_locations[white_options.index(s)])
                    for q in range(0, len(black_options)):
                        store = black_options[black_pieces.index('king')]
                        black_options[q] = [r for r in black_options[q] if r in white_checkers]
                        black_options[black_pieces.index('king')] = store

    # main game loop

    global white_options
    global black_options

    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')
    playcircle=pygame.draw.circle(screen, 'black', (40,175) , 50)
    playcounter=-1
    chess_run = True
  
    
    while chess_run:
        screen.blit(bg[color3-1], (280, 0))
        draw_menu()
        if playcounter == 1:
            play_pause = pygame.image.load('D:\\pygame\\SPYDR\\ch_play.png')
            play_pause = pygame.transform.scale(play_pause, (50, 50))
        elif playcounter == -1:
            play_pause = pygame.image.load('D:\\pygame\\SPYDR\\ch_pause.png')
            play_pause = pygame.transform.scale(play_pause, (50, 50))
        screen.blit(play_pause, (40,175))
        draw_board()
        draw_pieces()
        draw_captured()
        check_king(white_locations[white_pieces.index('king')], 'white')
        check_king(black_locations[black_pieces.index('king')], 'black')
        
        black_options = check_options(
            black_pieces, black_locations, 'black')
        white_options = check_options(
            white_pieces, white_locations, 'white')

        protect_king()
        
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                if playcircle.collidepoint(event.pos):
                    playcounter = -playcounter
                x_coord = (event.pos[0] - 340)// 65 
                y_coord = (event.pos[1] - 65) // 65
                click_coords = (x_coord, y_coord)
                if turn_step<= 1:   
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        white_unkillable = []
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                if turn_step > 1:                   
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_unkillable = []
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')

        if winner != '':
            game_over = True
            draw_game_over()

        pygame.display.flip()

while True:
    mainscreen()


