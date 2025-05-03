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

icon = pygame.image.load('E:\\pygame\\SPYDR\\icon.png')

pygame.display.set_caption("SPYDR Game Hub")
pygame.display.set_icon(icon)

#fonts
score_font= pygame.font.Font('E:\\pygame\\SPYDR\\score_ping-pong.ttf', 85)
resume_clock_font= pygame.font.Font('E:\\pygame\\SPYDR\\clock_ping-pong.otf', 50)
win_font= pygame.font.Font('E:\\pygame\\SPYDR\\winner_ping-pong.ttf', 80)
input_font= pygame.font.Font('E:\\pygame\\SPYDR\\input_ping-pong.otf', 30)
gamename_font= pygame.font.Font('E:\\pygame\\SPYDR\\input_ping-pong.otf', 40)
heading_font= pygame.font.Font('E:\\pygame\\SPYDR\\heading_ping-pong.ttf',110)
banner_font= pygame.font.Font('E:\\pygame\\SPYDR\\heading_ping-pong.ttf',40)
bannerbelow_font= pygame.font.Font('E:\\pygame\\SPYDR\\heading_ping-pong.ttf',30)
pause_font= pygame.font.Font('E:\\pygame\\SPYDR\\clock_ping-pong.otf', 25)

#sounds
button_sound = pygame.mixer.Sound('E:\\pygame\\SPYDR\\button.wav')
button_sound.set_volume(1)
bounce_sound = pygame.mixer.Sound('E:\\pygame\\SPYDR\\ball_bounce.wav')
bounce_sound.set_volume(1)
tick_sound = pygame.mixer.Sound('E:\\pygame\\SPYDR\\timer.wav')
tick_sound.set_volume(1)

#image load
main_bg = pygame.image.load("E:\\pygame\\SPYDR\\bg.png")
pingpong_thumb = pygame.image.load("E:\\pygame\\SPYDR\\pingpongthumbnail.jpg")
dino_thumb = pygame.image.load("E:\\pygame\\SPYDR\\dinothumbnail.png")
lucky_thumb = pygame.image.load("E:\\pygame\\SPYDR\\lsthumbnail.jpg")
chess_thumb = pygame.image.load("E:\\pygame\\SPYDR\\chessthumbnail.png")
ttt_thumb = pygame.image.load("E:\\pygame\\SPYDR\\tttthumbnail.jpg")
snl_thumb = pygame.image.load("E:\\pygame\\SPYDR\\snlthumbnail.jpg")

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
    
    screen.blit(dino_thumb,(445,166))
    dino_text = gamename_font.render('Dino', True, (255, 255, 255))
    dino_rect = dino_text.get_rect()
    dino_rect.center = 600,362
    screen.blit(dino_text, dino_rect)
    
    screen.blit(lucky_thumb,(790,166))
    lucky_text = gamename_font.render('Lucky 7', True, (255, 255, 255))
    lucky_rect = lucky_text.get_rect()
    lucky_rect.center = 945,362
    screen.blit(lucky_text, lucky_rect)
    
    screen.blit(chess_thumb,(100,423))
    chess_text = gamename_font.render('Chess', True, (255, 255, 255))
    chess_rect = chess_text.get_rect()
    chess_rect.center = 255,619
    screen.blit(chess_text, chess_rect)

    screen.blit(ttt_thumb,(445,423))
    ttt_text = gamename_font.render('Tic Tac Toe', True, (255, 255, 255))
    ttt_rect = ttt_text.get_rect()
    ttt_rect.center = 600,619
    screen.blit(ttt_text, ttt_rect)
    
    screen.blit(snl_thumb,(790,423))
    snl_text = gamename_font.render('Snakes and Ladders', True, (255, 255, 255))
    snl_rect = snl_text.get_rect()
    snl_rect.center = 945,619
    screen.blit(snl_text, snl_rect)

    for event in pygame.event.get():

        #cross button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pingpongarea = pygame.Rect(100, 166, 356, 157)
            if pingpongarea.collidepoint(event.pos) or pingpong_rect.collidepoint(event.pos):
                pp()
            dinoarea = pygame.Rect(445, 166, 356, 157)
            if dinoarea.collidepoint(event.pos) or dino_rect.collidepoint(event.pos):
                di()
            luckyarea = pygame.Rect(799, 166, 356, 157)
            if luckyarea.collidepoint(event.pos) or lucky_rect.collidepoint(event.pos):
                ls()
            chessarea = pygame.Rect(100, 423, 356, 157)
            if chessarea.collidepoint(event.pos) or chess_rect.collidepoint(event.pos):
                ch()
            tttarea = pygame.Rect(445, 423, 356, 157)
            if tttarea.collidepoint(event.pos) or ttt_rect.collidepoint(event.pos):
                ttt()
            snlarea = pygame.Rect(799, 423, 356, 157)
            if snlarea.collidepoint(event.pos) or snl_rect.collidepoint(event.pos):
                snl()
    
    pygame.display.flip()    

#----------------------------------------PING PONG----------------------------------------#

#image load

pi_play = pygame.image.load('E:\\pygame\\SPYDR\\pi_play.png')
pi_play = pygame.transform.scale(pi_play, (50, 50))

pi_pause = pygame.image.load('E:\\pygame\\SPYDR\\pi_pause.png')
pi_pause = pygame.transform.scale(pi_pause, (50, 50))

pi_play_pause = [pi_play, pi_pause]

pi_back = pygame.image.load('E:\\pygame\\SPYDR\\pi_back.png')
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
        bg = pygame.image.load("E:\\pygame\\SPYDR\\pingpong_bg.png")
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
              bg = pygame.image.load("E:\\pygame\\SPYDR\\pingpong_bg.png")
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
              bg = pygame.image.load("E:\\pygame\\SPYDR\\pingpong_bg.png")
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
bg1 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_1.png")
bg2 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_2.png")
bg3 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_3.png")
bg4 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_4.png")
bg5 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_5.png")
bg6 = pygame.image.load("E:\\pygame\\SPYDR\\ch_bg_6.png")
bg = [bg1, bg2, bg3, bg4, bg5, bg6]
banner = pygame.image.load('E:\\pygame\\SPYDR\\banner.png')
    
def ch():
    global winner
    global white_unkillable
    global black_unkillable
    global check
    global protect
    
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
    protect = False

    #game images
    black_queen = pygame.image.load('E:\\pygame\\SPYDR\\black queen.png')
    black_queen = pygame.transform.scale(black_queen, (45, 45))
    black_queen_small = pygame.transform.scale(black_queen, (20, 20))
    black_king = pygame.image.load('E:\\pygame\\SPYDR\\black king.png')
    black_king = pygame.transform.scale(black_king, (45, 45))
    black_king_small = pygame.transform.scale(black_king, (20, 20))
    black_rook = pygame.image.load('E:\\pygame\\SPYDR\\black rook.png')
    black_rook = pygame.transform.scale(black_rook, (45, 45))
    black_rook_small = pygame.transform.scale(black_rook, (20, 20))
    black_bishop = pygame.image.load('E:\\pygame\\SPYDR\\black bishop.png')
    black_bishop = pygame.transform.scale(black_bishop, (45, 45))
    black_bishop_small = pygame.transform.scale(black_bishop, (20, 20))
    black_knight = pygame.image.load('E:\\pygame\\SPYDR\\black knight.png')
    black_knight = pygame.transform.scale(black_knight, (45, 45))
    black_knight_small = pygame.transform.scale(black_knight, (20, 20))
    black_pawn = pygame.image.load('E:\\pygame\\SPYDR\\black pawn.png')
    black_pawn = pygame.transform.scale(black_pawn, (45, 45))
    black_pawn_small = pygame.transform.scale(black_pawn, (20, 20))
    white_queen = pygame.image.load('E:\\pygame\\SPYDR\\white queen.png')
    white_queen = pygame.transform.scale(white_queen, (45, 45))
    white_queen_small = pygame.transform.scale(white_queen, (20, 20))
    white_king = pygame.image.load('E:\\pygame\\SPYDR\\white king.png')
    white_king = pygame.transform.scale(white_king, (45, 45))
    white_king_small = pygame.transform.scale(white_king, (20, 20))
    white_rook = pygame.image.load('E:\\pygame\\SPYDR\\white rook.png')
    white_rook = pygame.transform.scale(white_rook, (45, 45))
    white_rook_small = pygame.transform.scale(white_rook, (20, 20))
    white_bishop = pygame.image.load('E:\\pygame\\SPYDR\\white bishop.png')
    white_bishop = pygame.transform.scale(white_bishop, (45, 45))
    white_bishop_small = pygame.transform.scale(white_bishop, (20, 20))
    white_knight = pygame.image.load('E:\\pygame\\SPYDR\\white knight.png')
    white_knight = pygame.transform.scale(white_knight, (45, 45))
    white_knight_small = pygame.transform.scale(white_knight, (20, 20))
    white_pawn = pygame.image.load('E:\\pygame\\SPYDR\\white pawn.png')
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
        global white_targets
        global black_targets
        colour = color
        king_moves_list = []
        black_targets = []
        white_targets = []
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
                        white_targets.append(king_target)
                        king_moves_list.append(king_target)
                if color == 'black':
                    if king_target not in white_unkillable:
                        black_targets.append(king_target)
                        king_moves_list.append(king_target)
                if protect == False:
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
        global black_targets
        global white_targets
        
        check = True
        black_checkers = [] 
        white_checkers = []
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        black_king_index = black_pieces.index('king')
        black_king_location = black_locations[black_king_index]
        white_king_index = white_pieces.index('king')
        white_king_location = white_locations[white_king_index]
        
        if colour == 'white':
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 65 + 1 +340,
                                                          white_locations[king_index][1] * 65 + 1 +65, 65, 65], 5)
                    
                for k in range(len(white_targets)-1, -1, -1):
                    king_target = white_targets[k]
                    
                    for o in black_options:
                        if king_target in o and king_target in white_targets:
                            white_targets.remove(king_target)
                            king_moves_list.remove(king_target)
                if white_targets == []:
                    checkers()
                            
        elif colour == 'black':
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]

            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 65 + 1 +340,
                                                          black_locations[king_index][1] * 65 + 1 +65, 65, 65], 5)
                    
                for k in range(len(black_targets)-1, -1, -1):
                    king_target = black_targets[k]
                                        
                    for o in white_options:
                        if king_target in o and king_target in black_targets:
                            black_targets.remove(king_target)
                            king_moves_list.remove(king_target)
                if black_targets == []:
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
                    lose = True
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

    def protect_king(color):
        global white_options
        global black_options
        global protect
        hi=0
        black_checkers = []
        white_checkers = []
        superlist_black_options = []
        superlist_white_options = []
        all_black_options = black_options.copy()
        all_white_options = white_options.copy()
        
        if color == 'white':

            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            
            for d in range(len(black_options)):
                all_black_options.extend(black_options[d])
                if king_location in black_options[d]:
                    for s in black_options:
                        if king_location in s:
                            black_checkers.append(black_locations[black_options.index(s)])
                    for q in range(0, len(white_options)):
                        store = white_options[white_pieces.index('king')]
                        white_options[q] = [r for r in white_options[q] if r in black_checkers]
                        white_options[white_pieces.index('king')] = store
                        
            
            for e in range(0, len(white_pieces)):
                store_white = white_locations[e]
                for v in all_white_options[e]:
                    white_locations[e] = v
                    protect = True
                    black_options = check_options(black_pieces, black_locations, 'black')
                    protect = False
                    for k in range (0, len(black_options)):
                        superlist_black_options.extend(black_options[k])
                    if king_location not in superlist_black_options:
                        if v not in white_options[e]:
                            white_options[e].append(v)
                    white_locations[e] = store_white
                    superlist_black_options = []
                        
        if color == 'black':

            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            
            for f in range(len(white_options)):
                all_white_options.extend(white_options[f])
                if king_location in white_options[f]:
                    for s in white_options:
                        if king_location in s:
                            white_checkers.append(white_locations[white_options.index(s)])
                    for q in range(0, len(black_options)):
                        store = black_options[black_pieces.index('king')]
                        black_options[q] = [r for r in black_options[q] if r in white_checkers]
                        black_options[black_pieces.index('king')] = store
                        
            if king_location not in all_white_options:
                for g in range(0, len(black_pieces)):
                    store_black = black_locations[g]
                    for v in black_options[g]:
                        black_locations[g] = v
                        protect = True
                        white_options = check_options(white_pieces, white_locations, 'white')
                        protect = False
                        for k in range (0, len(white_options)):
                            black_options[g] = [r for r in black_options[g] if king_location not in white_options[k]]
                        black_locations[g] = store_black
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
            play_pause = pygame.image.load('E:\\pygame\\SPYDR\\ch_play.png')
            play_pause = pygame.transform.scale(play_pause, (50, 50))
        elif playcounter == -1:
            play_pause = pygame.image.load('E:\\pygame\\SPYDR\\ch_pause.png')
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

        if turn_step<= 1:
            protect_king('white')
        #if turn_step> 1:
            #protect_king('black')
        
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

#------------------------------------------CHESS------------------------------------------#

#-------------------------------------------DINO------------------------------------------#

def di():

    y1 = 150
    y2 = 440
    screen.fill((240, 240, 240))
    pygame.display.flip()
    background = pygame.Surface((1200, y2- y1))
    background.fill((240, 240, 240))

    # BORDERS
    pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
    pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
    pygame.display.flip()

    # DINO
    sd1 = pygame.Surface((70, 70), pygame.SRCALPHA)
    dino = pygame.image.load("dino.png")
    dino = pygame.transform.scale(dino, (70, 70))
    dino1 = pygame.image.load("dino1.png")
    dino1 = pygame.transform.scale(dino1, (70, 70))
    dino2 = pygame.image.load("dino2.png")
    dino2 = pygame.transform.scale(dino2, (70, 70))
    dino3 = pygame.image.load("dino3.png")
    dino3 = pygame.transform.scale(dino3, (70, 70))
    dino4 = pygame.image.load("dino4.png")
    dino4 = pygame.transform.scale(dino4, (70, 70))
    dino_D = pygame.image.load("go1.png")
    go1 = pygame.transform.scale(dino_D, (70, 70))
    go2 = pygame.image.load("go2.png")


    # CACTUS
    cactus = pygame.image.load("cactus.png")
    sc1 = pygame.Surface((50, 50), pygame.SRCALPHA)
    cactus1 = pygame.transform.scale(cactus, (50, 50))
    sc2 = pygame.Surface((70, 70), pygame.SRCALPHA)
    cactus2 = pygame.transform.scale(cactus, (70, 70))

    # TIME VARIABLE
    t=0.003 

    # EXECUTION
    x=60
    y=50
    d=0
    i=0
    a=1200
    b=370
    score = 0
    state = True
    check = True
    while check:
        screen.blit(dino, (200, y2-70))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    sd1.fill((240, 240, 240))
                    # ACTUAL PROGRAM
                    while state:
                        #DINO_RUN 1 ------------------------------------------------------------
                        if i%6==0:
                            if a<200+x and a>200 and  b>=(y2-y-70):  #DIE
                                d=4
                                sd1.fill((240, 240, 240))
                                sd1.blit(go1, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                state = False
                                check = False
                                screen.blit(go2, (0,0))
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.display.quit(), sys.exit()
                                
                            else:  #CONTINUE
                                d=2
                                sd1.fill((240, 240, 240))
                                sd1.blit(dino1, (0,0))
                                screen.blit(sd1, (200, y2-70))

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.display.quit(), sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:   #JUMPPPP ---- 1
                                        for b in range(y2-70, y1+40, -1):  # UPPP
                                            if b>(y2-y-70) and a<200+x and a>200:  #DIE
                                                d=4
                                                sd1.fill((240, 240, 240))
                                                sd1.blit(go1, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))
                                                state = False
                                                check = False
                                                screen.blit(go2, (0,0))
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                #pygame.display.flip()
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.display.quit(), sys.exit()
                                                break
                                            else: #JUMP_CONTINUE
                                                d=1
                                                sd1.blit(dino, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))

                                            #CACTUS_CODE
                                            sc1.fill((240, 240, 240))
                                            sc1.blit(cactus1, (0,0))
                                            screen.blit(sc1, (a, y2-50))
                                            a-=1
                                            
                                             #DISPLAY
                                            pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                            pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                            pygame.display.flip()
                                            time.sleep(t)
                                        
                                        else:
                                            for b in range(y1+40, y2-70):  # DONWNNN
                                                if b>(y2-y-70) and a<200+x and a>200:  #DIE
                                                    d=4
                                                    sd1.fill((240, 240, 240))
                                                    sd1.blit(go1, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))
                                                    state = False
                                                    check = False
                                                    screen.blit(go2, (0,0))
                                                    pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                    pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                    #pygame.display.flip()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.display.quit(), sys.exit()
                                                    break
                                                else:  # JUMP_CONTINUE
                                                    d=0
                                                    sd1.blit(dino, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))

                                                #CACTUS_CODE
                                                sc1.fill((240, 240, 240))
                                                sc1.blit(cactus1, (0,0))
                                                screen.blit(sc1, (a, y2-50))
                                                a-=1

                                                #DISPLAY
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                pygame.display.flip()
                                                time.sleep(t)
                                                        
                        #DINO_RUN 2 ----------------------------------------------------------------------
                        elif i%6==3:
                            if a<200+x and a>200 and  b>=(y2-y-70):  #DIE
                                d=4
                                sd1.fill((240, 240, 240))
                                sd1.blit(go1, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                state = False
                                check = False
                                screen.blit(go2, (0,0))
                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.display.quit(), sys.exit()
                            else:
                                d=3
                                sd1.fill((240, 240, 240))
                                sd1.blit(dino2, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                             
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.display.quit(), sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE: #JUMPPP ---- 2
                                        for b in range(y2-70, y1+40, -1):  # UPPPPP
                                            if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                d=4
                                                sd1.fill((240, 240, 240))
                                                sd1.blit(go1, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))
                                                state = False
                                                check = False
                                                screen.blit(go2, (0,0))
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                #pygame.display.flip()
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.display.quit(), sys.exit()
                                                break
                                            else:  # JUMP_CONTINUE
                                                d=1
                                                sd1.blit(dino, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))

                                            #CACTUS_CODE
                                            sc1.fill((240, 240, 240))
                                            sc1.blit(cactus1, (0,0))
                                            screen.blit(sc1, (a, y2-50))
                                            a-=1

                                            #DISPLAY
                                            pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                            pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                            pygame.display.flip()
                                            time.sleep(t)
                                        
                                        else:
                                            for b in range(y1+40, y2-70): # DONWNNN
                                                if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                    d=4
                                                    sd1.fill((240, 240, 240))
                                                    sd1.blit(go1, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))
                                                    state = False
                                                    check = False
                                                    screen.blit(go2, (0,0))
                                                    pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                    pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                    #pygame.display.flip()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.display.quit(), sys.exit()
                                                    break
                                                else:  # JUMP_CONTINUE
                                                    d=0
                                                    sd1.blit(dino, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))

                                                #CACTUS_CODE
                                                sc1.fill((240, 240, 240))
                                                sc1.blit(cactus1, (0,0))
                                                screen.blit(sc1, (a, y2-50))
                                                a-=1

                                                #DISPLAY
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                pygame.display.flip()
                                                time.sleep(t)

                        #DINO_RUN_ LEGS MIX   -------------------------------------------------------------------
                        elif i%6==2 or i%6==5:
                            if a<200+x and a>200 and  b>=(y2-y-70):  #DIE
                                d=4
                                sd1.fill((240, 240, 240))
                                sd1.blit(go1, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                state = False
                                check = False
                                screen.blit(go2, (0,0))
                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.display.quit(), sys.exit()
                            else:
                                d=3
                                sd1.fill((240, 240, 240))
                                sd1.blit(dino3, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                             
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.display.quit(), sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE: #JUMPPP ---- 2
                                        for b in range(y2-70, y1+40, -1):  # UPPPPP
                                            if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                d=4
                                                sd1.fill((240, 240, 240))
                                                sd1.blit(go1, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))
                                                state = False
                                                check = False
                                                screen.blit(go2, (0,0))
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                #pygame.display.flip()
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.display.quit(), sys.exit()
                                                break
                                            else:  # JUMP_CONTINUE
                                                d=1
                                                sd1.blit(dino, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))

                                            #CACTUS_CODE
                                            sc1.fill((240, 240, 240))
                                            sc1.blit(cactus1, (0,0))
                                            screen.blit(sc1, (a, y2-50))
                                            a-=1

                                            #DISPLAY
                                            pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                            pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                            pygame.display.flip()
                                            time.sleep(t)
                                        
                                        else:
                                            for b in range(y1+40, y2-70): # DONWNNN
                                                if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                    d=4
                                                    sd1.fill((240, 240, 240))
                                                    sd1.blit(go1, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))
                                                    state = False
                                                    check = False
                                                    screen.blit(go2, (0,0))
                                                    pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                    pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                    #pygame.display.flip()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.display.quit(), sys.exit()
                                                    break
                                                else:  # JUMP_CONTINUE
                                                    d=0
                                                    sd1.blit(dino, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))

                                                #CACTUS_CODE
                                                sc1.fill((240, 240, 240))
                                                sc1.blit(cactus1, (0,0))
                                                screen.blit(sc1, (a, y2-50))
                                                a-=1

                                                #DISPLAY
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                pygame.display.flip()
                                                time.sleep(t)

                        #DINO_RUN_ STANDING POSITION   -------------------------------------------
                        elif i%6==1 or i%6==4:
                            if a<200+x and a>200 and  b>=(y2-y-70):  
                                d=4
                                sd1.fill((240, 240, 240))
                                sd1.blit(go1, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                state = False
                                check = False
                                screen.blit(go2, (0,0))
                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.display.quit(), sys.exit()

                            else:
                                d=3
                                sd1.fill((240, 240, 240))
                                sd1.blit(dino4, (0,0))
                                screen.blit(sd1, (200, y2-70))
                                             
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.display.quit(), sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE: #JUMPPP ---- 2
                                        for b in range(y2-70, y1+40, -1):  # UPPPPP
                                            if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                d=4
                                                sd1.fill((240, 240, 240))
                                                sd1.blit(go1, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))
                                                state = False
                                                check = False
                                                screen.blit(go2, (0,0))
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                #pygame.display.flip()
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.display.quit(), sys.exit()
                                                break
                                            else:  # JUMP_CONTINUE
                                                d=1
                                                sd1.blit(dino, (0, 0))
                                                screen.blit(background, (0,y1))
                                                screen.blit(sd1, (200, b))

                                            #CACTUS_CODE
                                            sc1.fill((240, 240, 240))
                                            sc1.blit(cactus1, (0,0))
                                            screen.blit(sc1, (a, y2-50))
                                            a-=1

                                            #DISPLAY
                                            pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                            pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                            pygame.display.flip()
                                            time.sleep(t)
                                        
                                        else:
                                            for b in range(y1+40, y2-70): # DONWNNN
                                                if b>(y2-y-70) and a<200+x and a>200: #DIEEE
                                                    d=4
                                                    sd1.fill((240, 240, 240))
                                                    sd1.blit(go1, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))
                                                    state = False
                                                    check = False
                                                    screen.blit(go2, (0,0))
                                                    pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                    pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                    #pygame.display.flip()
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.display.quit(), sys.exit()
                                                    break
                                                else:  # JUMP_CONTINUE
                                                    d=0
                                                    sd1.blit(dino, (0, 0))
                                                    screen.blit(background, (0,y1))
                                                    screen.blit(sd1, (200, b))

                                                #CACTUS_CODE
                                                sc1.fill((240, 240, 240))
                                                sc1.blit(cactus1, (0,0))
                                                screen.blit(sc1, (a, y2-50))
                                                a-=1

                                                #DISPLAY
                                                pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                                                pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                                                pygame.display.flip()
                                                time.sleep(t)

                                                
                        #CACTUS_CODE
                        sc1.fill((240, 240, 240))
                        sc1.blit(cactus1, (0,0))
                        screen.blit(sc1, (a, y2-50))
                        i+=1
                        a-=3
                        if a < -70:
                            a=1200
                            t=(2*t)/3
                            score = score + 1
                        
                        #DISPLAY
                        pygame.draw.line(screen, (0,0,0), (0, y2), (1200, y2), 3)
                        pygame.draw.line(screen, (0,0,0), (0, y1), (1200, y1), 3)
                        pygame.display.flip()
                        time.sleep(t)
                        

#-------------------------------------------DINO------------------------------------------#
                        
#-----------------------------------------LUCKY 7-----------------------------------------#                        
                        
def ls():
    c=0
    z=5
    x=4
    #Black screen
    black = pygame.image.load("black.jpg")
    black = pygame.transform.scale(black, (1200, 650))

    #screen setup
    screen.blit(black, (0,0))
    pygame.display.flip()

    # Images ------------------------------------------------------------
    # Intro
    s1 = pygame.Surface((500, 150), pygame.SRCALPHA)
    intro = pygame.image.load("Lucky 7.png")
    # Dices
    s2 = pygame.Surface((200, 200), pygame.SRCALPHA)
    dice1 = pygame.image.load("dice1.png")
    dice1 = pygame.transform.scale(dice1, (200, 200))
    dice2 = pygame.image.load("dice2.png")
    dice2 = pygame.transform.scale(dice2, (200, 200))
    dice3 = pygame.image.load("dice3.png")
    dice3 = pygame.transform.scale(dice3, (200, 200))
    dice4 = pygame.image.load("dice4.png")
    dice4 = pygame.transform.scale(dice4, (200, 200))
    dice5 = pygame.image.load("dice5.png")
    dice5 = pygame.transform.scale(dice5, (200, 200))
    dice6 = pygame.image.load("dice6.png")
    dice6 = pygame.transform.scale(dice6, (200, 200))
    # Choose
    s3 = pygame.Surface((250, 250), pygame.SRCALPHA)
    A7 = pygame.image.load("Above7.png")
    A7 = pygame.transform.scale(A7, (250, 250))
    B7 = pygame.image.load("Below7.png")
    B7 = pygame.transform.scale(B7, (250, 250))
    O7 = pygame.image.load("Or7.png")
    O7 = pygame.transform.scale(O7, (250, 250))
    # Numbers
    n1 = pygame.image.load("n1.png")
    n1 = pygame.transform.scale(n1, (100, 100))
    n2 = pygame.image.load("n2.png")
    n2 = pygame.transform.scale(n2, (100, 100))
    n3 = pygame.image.load("n3.png")
    n3 = pygame.transform.scale(n3, (100, 100))
    n4 = pygame.image.load("n4.png")
    n4 = pygame.transform.scale(n4, (100, 100))
    n5 = pygame.image.load("n5.png")
    n5 = pygame.transform.scale(n5, (100, 100))
    n6 = pygame.image.load("n6.png")
    n6 = pygame.transform.scale(n6, (100, 100))
    #WIN/LOSE
    won = pygame.image.load("won.png")
    lose = pygame.image.load("lose.png")
    # BUTTONS
    button1 = pygame.Rect(150, 300, 250, 250)
    button2 = pygame.Rect(450, 300, 250, 250)
    button3 = pygame.Rect(750, 300, 250, 250)
    button4 = pygame.Rect(471, 345, 174, 174) # Retry


    #CLosing Function
    def close():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

    for event in pygame.event.get():
        close()

    check = True
    while check:   # START __________________________________________________________________________________________________________________________
        #Displaying the intro and buttons
        screen.blit(intro, (350, 50))
        pygame.display.flip()
        screen.blit(B7, (150, 300))
        pygame.display.flip()
        screen.blit(O7, (450, 300))
        pygame.display.flip()
        screen.blit(A7, (750, 300))
        pygame.display.flip()
        for event in pygame.event.get():  # EVENT DETECTED
            close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if button1.collidepoint(event.pos): # BELOW 7
                    screen.blit(black, (0,0))
                    pygame.display.flip()
                    for i in range(1, 10):
                        for event in pygame.event.get():   #CLose Option
                            close()
                        a=random.randrange(1,7) # Dice 1
                        if a==1:
                            screen.blit(dice1, (400, 200))
                        elif a==2:
                            screen.blit(dice2, (400, 200))
                        elif a==3:
                            screen.blit(dice3, (400, 200))
                        elif a==4:
                            screen.blit(dice4, (400, 200))
                        elif a==5:
                            screen.blit(dice5, (400, 200))
                        elif a==6:
                            screen.blit(dice6, (400, 200))

                        b=random.randrange(7,13) # Dice 2
                        if b==7:
                            screen.blit(dice1, (600, 200))
                        elif b==8:
                            screen.blit(dice2, (600, 200))
                        elif b==9:
                            screen.blit(dice3, (600, 200))
                        elif b==10:
                            screen.blit(dice4, (600, 200))
                        elif b==11:
                            screen.blit(dice5, (600, 200))
                        elif b==12:
                            screen.blit(dice6, (600, 200))

                        pygame.display.flip() #Display
                        time.sleep(0.1)
                        
                    else:      # Printing the numbers
                        if a==1:         
                            screen.blit(n1, (450, 400))
                        if a==2:
                            screen.blit(n2, (450, 400))
                        if a==3:
                            screen.blit(n3, (450, 400))
                        if a==4:
                            screen.blit(n4, (450, 400))
                        if a==5:
                            screen.blit(n5, (450, 400))
                        if a==6:
                            screen.blit(n6, (450, 400))
                        if b==7:
                            screen.blit(n1, (650, 400))
                            b=1
                        if b==8:
                            screen.blit(n2, (650,400))
                            b=2
                        if b==9:
                            screen.blit(n3, (650,400))
                            b=3
                        if b==10:
                            screen.blit(n4, (650,400))
                            b=4
                        if b==11:
                            screen.blit(n5, (650, 400))
                            b=5
                        if b==12:
                            screen.blit(n6, (650, 400))
                            b=6
                        pygame.display.flip()
                        time.sleep(2)
                        c=a+b
                        print(c)

                    if c<7:
                        screen.blit(won, (0,0))
                        pygame.display.flip()
                    else:
                        screen.blit(lose, (0,0))
                        pygame.display.flip()
                    time.sleep(3)
                    for event in pygame.event.get():
                        close()
                        # --------------------------------------------------------------------------------------------
                if button2.collidepoint(event.pos): #  7
                    screen.blit(black, (0,0))
                    pygame.display.flip()
                    for i in range(1, 10):
                        for event in pygame.event.get():   #CLose Option
                            close()
                            
                        a=random.randrange(1,7) # Dice 1
                        if a==1:
                            screen.blit(dice1, (400, 200))
                        elif a==2:
                            screen.blit(dice2, (400, 200))
                        elif a==3:
                            screen.blit(dice3, (400, 200))
                        elif a==4:
                            screen.blit(dice4, (400, 200))
                        elif a==5:
                            screen.blit(dice5, (400, 200))
                        elif a==6:
                            screen.blit(dice6, (400, 200))

                        b=random.randrange(7,13) # Dice 2
                        if b==7:
                            screen.blit(dice1, (600, 200))
                        elif b==8:
                            screen.blit(dice2, (600, 200))
                        elif b==9:
                            screen.blit(dice3, (600, 200))
                        elif b==10:
                            screen.blit(dice4, (600, 200))
                        elif b==11:
                            screen.blit(dice5, (600, 200))
                        elif b==12:
                            screen.blit(dice6, (600, 200))

                        pygame.display.flip() #Display
                        time.sleep(0.1)
                        
                    else:      # Printing the numbers
                        if a==1:         
                            screen.blit(n1, (450, 400))
                        if a==2:
                            screen.blit(n2, (450, 400))
                        if a==3:
                            screen.blit(n3, (450, 400))
                        if a==4:
                            screen.blit(n4, (450, 400))
                        if a==5:
                            screen.blit(n5, (450, 400))
                        if a==6:
                            screen.blit(n6, (450, 400))
                        if b==7:
                            screen.blit(n1, (650, 400))
                            b=1
                        if b==8:
                            screen.blit(n2, (650,400))
                            b=2
                        if b==9:
                            screen.blit(n3, (650,400))
                            b=3
                        if b==10:
                            screen.blit(n4, (650,400))
                            b=4
                        if b==11:
                            screen.blit(n5, (650, 400))
                            b=5
                        if b==12:
                            screen.blit(n6, (650, 400))
                            b=6
                        pygame.display.flip()
                        time.sleep(2)
                        c=a+b
                        print(c)

                    if c==7:
                        screen.blit(won, (0,0))
                        pygame.display.flip()
                    else:
                        screen.blit(lose, (0,0))
                        pygame.display.flip()
                    time.sleep(3)
                    for event in pygame.event.get():
                        close()

                # ----------------------------------------------------------------------------------------
                if button3.collidepoint(event.pos): # ABOVE 7
                    screen.blit(black, (0,0))
                    pygame.display.flip()
                    for i in range(1, 10):
                        for event in pygame.event.get():   #CLose Option
                            close()
                            
                        a=random.randrange(1,7) # Dice 1
                        if a==1:
                            screen.blit(dice1, (400, 200))
                        elif a==2:
                            screen.blit(dice2, (400, 200))
                        elif a==3:
                            screen.blit(dice3, (400, 200))
                        elif a==4:
                            screen.blit(dice4, (400, 200))
                        elif a==5:
                            screen.blit(dice5, (400, 200))
                        elif a==6:
                            screen.blit(dice6, (400, 200))

                        b=random.randrange(7,13) # Dice 2
                        if b==7:
                            screen.blit(dice1, (600, 200))
                        elif b==8:
                            screen.blit(dice2, (600, 200))
                        elif b==9:
                            screen.blit(dice3, (600, 200))
                        elif b==10:
                            screen.blit(dice4, (600, 200))
                        elif b==11:
                            screen.blit(dice5, (600, 200))
                        elif b==12:
                            screen.blit(dice6, (600, 200))

                        pygame.display.flip() #Display
                        time.sleep(0.1)
                        
                    else:      # Printing the numbers
                        if a==1:         
                            screen.blit(n1, (450, 400))
                        if a==2:
                            screen.blit(n2, (450, 400))
                        if a==3:
                            screen.blit(n3, (450, 400))
                        if a==4:
                            screen.blit(n4, (450, 400))
                        if a==5:
                            screen.blit(n5, (450, 400))
                        if a==6:
                            screen.blit(n6, (450, 400))
                        if b==7:
                            screen.blit(n1, (650, 400))
                            b=1
                        if b==8:
                            screen.blit(n2, (650,400))
                            b=2
                        if b==9:
                            screen.blit(n3, (650,400))
                            b=3
                        if b==10:
                            screen.blit(n4, (650,400))
                            b=4
                        if b==11:
                            screen.blit(n5, (650, 400))
                            b=5
                        if b==12:
                            screen.blit(n6, (650, 400))
                            b=6
                        pygame.display.flip()
                        time.sleep(2)
                        c=a+b
                        print(c)

                    if c>7:
                        screen.blit(won, (0,0))
                        pygame.display.flip()
                    else:
                        screen.blit(lose, (0,0))
                        pygame.display.flip()
                    time.sleep(3)
                    for event in pygame.event.get():
                        close()
                        
#-----------------------------------------LUCKY 7-----------------------------------------#

#-------------------------------------------TTT-------------------------------------------#

#defined variables
game_over=False
clicked=False
poss=[]
player=1
green0= (0,255,0)
red0= (255,0,0)
blue0=(0,0,255)
white0=(255,255,255)
black0=(0,0,0)
yellow0=(255,255,0)
cell_x_n=0
cell_y_n=0
winner=0
game_over = False
font=pygame.font.SysFont(None,100)
font_small=pygame.font.SysFont(None, 40)
font_sup_small=pygame.font.SysFont(None, 25)
again_rect=Rect(1200//2-82, 650//2+28, 165, 30)
exit_rect=Rect(10, 10, 185,30)


#play area n game grid
def play_area():
    bg_color=(144, 238, 144)
    screen.fill(bg_color)
    
    area_color=(0,0,0)
    border_color=(0,0,255)
    pygame.draw.rect(screen, border_color, pygame.Rect(295,20,610,610),5)
    pygame.draw.rect(screen, area_color, pygame.Rect(300,25,600,600))
    
def draw_grid():
    grid_color=(255,255,255)
    grid_width=6
    for x in range(1,3):
        pygame.draw.line(screen, grid_color, (300,(x*200)+25), (899,(x*200)+25), grid_width)
        pygame.draw.line(screen, grid_color, ((x*200)+300,25), ((x*200)+300,624), grid_width)

    
#the gird board
markers=[]
for x in range(3):
    row=[0]*3
    markers.append(row)


#game logic + drawing markers
def draw_markers():
    x_poss=0
    for x in markers:
        y_poss=0
        for y in x:
            if y==1:

                pygame.draw.line(screen, green0, ((x_poss*200)+315,(y_poss*200)+40), ((x_poss*200)+485,(y_poss*200)+210), 6)
                pygame.draw.line(screen, green0, ((x_poss*200)+315,(y_poss*200)+210), ((x_poss*200)+485,(y_poss*200)+40), 6)

            elif y==-1:
                pygame.draw.circle(screen, red0, ((x_poss*200)+402.5,(y_poss*200)+125),90,6)

            y_poss+=1
        x_poss+=1

    
#winner cheking
def check_winner():
    global winner
    global game_over
    a=0
    y_poss=0
    for x in markers:
        #direct colums wins
        if sum(x)==3:
            winner=1
            game_over=True
        if sum(x)==-3:
            winner=2
            game_over=True
            
        #direct rows wins
        if markers[0][y_poss]+markers[1][y_poss]+markers[2][y_poss]==3:
            winner=1
            game_over=True
        if markers[0][y_poss]+markers[1][y_poss]+markers[2][y_poss]==-3:
            winner=2
            game_over=True
        y_poss+=1

    #cross wins
    if markers[0][0]+markers[1][1]+markers[2][2]==3:
        winner=1
        game_over=True
    if markers[2][0]+markers[1][1]+markers[0][2]==3:
        winner=1
        game_over=True
    if markers[0][0]+markers[1][1]+markers[2][2]==-3:
        winner=2
        game_over=True
    if markers[2][0]+markers[1][1]+markers[0][2]==-3:
        winner=2
        game_over=True

    #draw 
    for i in markers:
        for j in i:
            if winner==0 and j!=0:
                a+=1
    if a==9:
        winner=None
        game_over=True


#announce the winner
def draw_winner(winner):
    if winner!=None:
        win_text='PLAYER '+str(winner)+' WINS!'
        win_img=font.render(win_text,True,blue0)
    elif winner==None:
        win_text='IT IS A DRAW!'
        win_img=font.render(win_text,True,blue0)

    if winner==1:
        pygame.draw.rect(screen, green0, (1200//3-85, 650//2-60, 570, 80))
        screen.blit(win_img, (1200//3-75, 650//2-50))
    elif winner==2:
        pygame.draw.rect(screen, red0, (1200//3-85, 650//2-60, 570, 80))
        screen.blit(win_img, (1200//3-75, 650//2-50))
    elif winner==None:
        pygame.draw.rect(screen, yellow00, (1200//3-50, 650//2-60, 495, 80))
        screen.blit(win_img, (1200//3-40, 650//2-50))


    again_text= 'Play Again?'
    again_img = font_small.render(again_text, True, black0)

    exit_text='Tap esc button to exit'
    exit_img= font_sup_small.render(exit_text, True, black0)
    
    pygame.draw.rect(screen, yellow0,again_rect)
    screen.blit(again_img,(1200//2-80, 650//2+30))
    
    pygame.draw.rect(screen, yellow0,exit_rect)
    screen.blit(exit_img,(15, 15))

def ttt():
    global game_over
    global clicked
    global markers
    global player
    global winner
    #game loop
    run=True
    while run:
        
        play_area()
        draw_grid()
        draw_markers()


        #event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if game_over ==0:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked==False:
                    clicked=True
                if event.type == pygame.MOUSEBUTTONUP and clicked==True:
                    clicked=False
                    poss=pygame.mouse.get_pos()
                    cell_x=poss[0]
                    cell_y=poss[1]

                    #define cells for the grid
                    if cell_x>300 and cell_y>25 and cell_x<900 and cell_y<625:

                        if cell_x>300 and cell_x<500:
                            cell_x_n=cell_x_n+0
                        elif cell_x>500 and cell_x<700:
                            cell_x_n=cell_x_n+1
                        elif cell_x>700 and cell_x<900:
                            cell_x_n=cell_x_n+2
                        else:
                            pass
                
                        if cell_y>25 and cell_y<225:
                            cell_y_n=cell_y_n+0
                        elif cell_y>225 and cell_y<425:
                            cell_y_n=cell_y_n+1
                        elif cell_y>425 and cell_y<625:
                            cell_y_n=cell_y_n+2
                        else:
                            pass  

                    #define points n turns
                    if markers[cell_x_n][cell_y_n]==0:
                        markers[cell_x_n][cell_y_n]=player
                        player *= -1

                        check_winner()

        if game_over==True:
            draw_winner(winner)
            
            #play again button
            if event.type == pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type == pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                poss=pygame.mouse.get_pos()
                if again_rect.collidepoint(poss):
                    #reset imp variables
                    markers=[]
                    poss=[]
                    player=1
                    winner=0
                    game_over=False
                    for x in range(3):
                        row=[0]*3
                        markers.append(row)
            if event.type == pygame.KEYDOWN:
               if event.key == K_ESCAPE:
                   break
                   
        cell_y_n,cell_x_n=0,0

        pygame.display.update()      
   

#-------------------------------------------TTT-------------------------------------------#

#-------------------------------------------SNL-------------------------------------------#

clock=pygame.time.Clock()
w=1200
h=650
#Graphics:
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("Snakes-and-Ladders-Bigger.jpg")
dice11=pygame.image.load("Dice11.png")
dice22=pygame.image.load("Dice22.png")
dice33=pygame.image.load("Dice33.png")
dice44=pygame.image.load("Dice44.png")
dice55=pygame.image.load("Dice55.png")
dice66=pygame.image.load("Dice66.png")

redgoti=pygame.image.load("redgoti.png")
yellowgoti=pygame.image.load("yellowgoti.png")
greengoti=pygame.image.load("greengoti.png")
bluegoti=pygame.image.load("bluegoti.png")
menubg=pygame.image.load("menu.jpg")
p=pygame.image.load("playbg.jpg")

intbg2=pygame.image.load("intropic2.jpg")

intbg3=pygame.image.load("intropic3.jpg")

intbg4=pygame.image.load("intropic4.jpg")

intbg5=pygame.image.load("intropic5.jpg")



#mouse pos
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()


#Message displaying for buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

   

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#Message displaying for field
def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)
    

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

#Goti movement function
def goti(a):
    l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
    l2=l1[a]
    x=l2[0]-25
    y=l2[1]-25
    return x,y
     

def text_objects1(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()

#Ladder check
def ladders(x):
    if x==1: return 38
    elif x==4:return 14
    elif x==9:return 31
    elif x==28:return 84
    elif x==21:return 42
    elif x==51:return 67
    elif x==80:return 99
    elif x==72:return 91
    else:return x

#Snake Check
def snakes(x): 
    if x==17:return 7
    elif x==54:return 34
    elif x==62:return 19
    elif x==64:return 60
    elif x==87:return 36
    elif x==93:return 73
    elif x==95: return 75
    elif x==98: return 79
    else:return x

def dice(a):
    if a==1:
        a=dice11
    elif a==2:
        a=dice22
    elif a==3:
        a=dice33
    elif a==4:
        a=dice44
    elif a==5:
        a=dice55
    elif a==6:
        a=dice66

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        screen.blit(a,(134,382))
        pygame.display.update()    



#Buttons for playing:
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(screen,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(screen,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
    

#Turn
def turn(score,l,s):
    
    a=randint(1,6)#player dice roll
    if a==6:
        six=True
    else:
        six=False
    p=dice(a)
    score+=a
    if score<=100:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            
            time=pygame.time.get_ticks()
            score=lad 
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            
            score=snk
           
    else: #checks if player score is not grater than 100
        score-=a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
    return score,l,s,six
    

#Quitting:
def Quit():
    pygame.quit()
    quit()

#Buttons:
def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(screen,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
            elif b=="s" or b==2 or b==3 or b==4:
                return b
            elif b==7:
                options()
            else :return True
                
            
            
            
                
            
    else:
        pygame.draw.rect(screen,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)


#def pause():
    #j=True
    #while j:
        #mouse pos
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #screen.blit(pause_bg,(0,0))
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #if button("Resume",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,10):
            #j=False
        #if button("Main Menu",mouse[0],mouse[1],(w/2)-150,500,300,50,red,b_red,30,10):
            #main()
        #pygame.display.update()
    
def intro():
    
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            screen.blit(intbg2,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            screen.blit(intbg3,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            screen.blit(intbg4,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            screen.blit(intbg5,(0,0))
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()


    
#Main Menu
def main():
        
    

    
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        screen.blit(menubg,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)


        
        pygame.display.update()


#Options Menu:
def options():
    
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b3=b4=b5=-1
        screen.blit(menubg,(0,0))
        #Single player button
        b1=button("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
        #2 player button
        b2=button("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
        #3 player
        b3=button("3 Players",mouse[0],mouse[1],(w/2)-150,450,300,50,green,b_green,30,3)
        #4 player
        b4=button("4 Players",mouse[0],mouse[1],(w/2)-150,550,300,50,green,b_green,30,4)
        #Back button
        b5=button("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
        if b5==5:
            main()
        if b1=="s":
            play(21)
        if b2==2:
            play(2)
        if b3==3:
            play(3)
        if b4==4:
            play(4)
        
        pygame.display.update()

def play(b):

    
    b6=-1
    time=3000
    if b6==7:
        options()
    screen.blit(p,(0,0))
    screen.blit(board,(433,134))
    xcr=xcy=xcg=xcb=406-25
    ycr=ycy=ycg=ycb=606-25
    screen.blit(redgoti,(xcy,ycy))
    if 5>b>1 or b==21:
        screen.blit(yellowgoti,(xcy,ycy))
            
    if 5>b>2 or b==21:
        screen.blit(greengoti,(xcg,ycg))
            
    if 5>b>2:
        screen.blit(bluegoti,(xcb,ycb))
    p1="Player 1"
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2="Player 2"
        p2score=0
    if 5>b>2:
        p3="Player 3"
        p3score=0
    if 5>b>3:
        p4="Player 4"
        p4score=0
    t=1
    play=True
    while True:
        l=False
        s=False
        time=3000
        screen.blit(p,(0,0))
        screen.blit(board,(433,134))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

            
        if b==21:
            #(player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)
            
            if button1("Player 1",mouse[0],mouse[1],100,650,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    if not six:
                        t+=1
                    xcr,ycr=goti(p1score)
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break
            
            button1("Computer",mouse[0],mouse[1],400,650,200,50,yellow,grey,30)
            if True:
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3 or b==21:
                            t=1
                    
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Computer Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break
        if 5>b>1:
            if button1("Player 1",mouse[0],mouse[1],100,650,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    xcr,ycr=goti(p1score)
                    if not six:
                        t+=1
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break
                
            if button1("Player 2",mouse[0],mouse[1],400,650,200,50,yellow,grey,30):
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3:
                            t=1
                    
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 2 Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break
                
        if 5>b>2:
            if button1("Player 3",mouse[0],mouse[1],700,650,200,50,green,grey,30):
                if t==3:
                    p3score,l,s,six=turn(p3score,l,s)
                    xcg,ycg=goti(p3score)
                    if not six:
                        t+=1
                        if b<4:
                            t=1
                    
                    if p3score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 3 Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break
                
        if 5>b>3:   
            if button1("Player 4",mouse[0],mouse[1],1000,650,200,50,blue,grey,30):
                if t==4:
                    p4score,l,s,six=turn(p4score,l,s)
                    xcb,ycb=goti(p4score)
                    if not six:
                        t+=1
                        if b<5:
                            t=1
                    
                    if p4score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 4 Wins",650,50,50,black)
                            
                            pygame.display.update()
                        break

        
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        screen.blit(redgoti,(xcr,ycr))
        if 5>b>1 or b==21:
            screen.blit(yellowgoti,(xcy+2,ycy))
            
            
        if 5>b>2:
            screen.blit(greengoti,(xcg+4,ycg))
            
             
        if 5>b>3:
            screen.blit(bluegoti,(xcb+6,ycb))
            
        if l:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Ladder!",650,50,35,black)
                pygame.display.update()
        if s:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Snake!",650,50,35,black)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()
        
            
def snl():
    intro()
    main()

        
#-------------------------------------------SNL-------------------------------------------#

while True:
    mainscreen()


