import pygame
import sys
import random
import math


# initialize pygame screen
pygame.init()

displayWidth = 640
displayHeight = 480

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

screen = pygame.display.set_mode((displayWidth,displayHeight))


# console menu

print()
print("Press space bar to start game and launch ball")
print()
print("PLAYER ONE: (Left) ")
print("Press 'w' to move up, 's' to move down")
print("PLAYER TWO: (Right) ")
print("Press 'Up' to move up, 'Down' to move down")
print()
print("Press 'esc' to exit")
print()


class StartButton:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 250
        self.height = 80
        self.rect = pygame.Rect(x,y,self.width,self.height)
    def render(self):
        pygame.draw.rect(screen,pygame.Color('lightsalmon'),(self.x,self.y,self.width,self.height))
    def render2(self):
        pygame.draw.rect(screen,pygame.Color('darksalmon'),(self.x,self.y,self.width,self.height))

class Circle(pygame.sprite.Sprite):   
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x=x
        self.y=y

        self.rect = self.image.get_rect()
 
    def render(self):
        screen.blit(self.image, (self.x,self.y))

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.image = pygame.Surface([w,h])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    def render(self):
        screen.blit(self.image, (self.x, self.y))


# start of game setup

gameOver = False
winner = False
play = False
ball_moving = False

blockWidth = 30
blockLength = 70
blockColor1 = pygame.Color('royalblue1')
blockColor2 = pygame.Color('mediumspringgreen')
yPos1 = int((displayHeight/2)-(blockLength/2))
yPos2 = int((displayHeight/2)-(blockLength/2))
yPos1_change = 0
yPos2_change = 0
INITIALSPEED = 5
speed = INITIALSPEED
MAXSPEED = 20
score1 = 0
score2 = 0

beachBall = pygame.image.load("circle.png").convert_alpha()
image = pygame.transform.scale(beachBall, (40,40))
ball = Circle(image, 300, 220)

block1 = Block(blockColor1, 0, yPos1, blockWidth, blockLength) #left block
block2 = Block(blockColor2, 610, yPos2, blockWidth, blockLength) #right block

# place ball at center of screen and determine launch angle
def restart():
    angle1 = random.randint(134, 225)
    angle2 = random.randint(-46,45)
    angleChoose = random.randint(0,1)
    global angle, counter_changex, counter_changey, ball_moving, speed
    if angleChoose == 0:
        angle = angle1
    elif angleChoose == 1:
        angle = angle2
    ball_moving = False
    counter_changex = 0
    counter_changey = 0
    ball.x = 300
    ball.y = 220
    speed = INITIALSPEED


# start screen

button = StartButton(int(displayWidth/2-125), int(displayHeight/2-40))
inputboxcolor = (235, 235, 235)
active = False
inputtext = ""

while not play:
    clock.tick(60)
    pygame.display.flip()
    screen.fill(pygame.Color('paleturquoise2'))

    # play button and score input

    button.render()
    if button.rect.collidepoint(pygame.mouse.get_pos()):
        button.render2()
    playfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 130)
    playtext = playfont.render("PLAY", True, (255, 255, 255))
    screen.blit(playtext, (int(displayWidth/2-118),int(displayHeight/2-40)))

    pointsfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 26)
    pointstext = pointsfont.render("Enter the winning score: ", True, (0, 0 ,0))
    screen.blit(pointstext, (int(displayWidth/2-125),int(displayHeight/2 + 60)))

    inputbox = pygame.Rect(int(displayWidth/2+85), int(displayHeight/2 + 56), 40, 20)
    coloractive = (255,255,255)
    colorinactive = (235, 235, 235)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
            gameOver = True
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_ESCAPE:
                play = True
                gameOver = True
            if event.key == pygame.K_SPACE:
                play = True
                restart()
        # click play 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button.rect.collidepoint(pos):               
                play = True
                restart()
        # change color of input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputbox.collidepoint(event.pos):
                inputboxcolor = coloractive
                active = True
            else:
                inputboxcolor = colorinactive
                active = False
        # read input text
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    active = False
                    inputboxcolor = colorinactive
                elif event.key == pygame.K_BACKSPACE:
                    inputtext = inputtext[:-1]
                else:
                    inputtext += event.unicode
        
    pygame.draw.rect(screen, inputboxcolor, inputbox)
    if inputtext or active: 
        textsurface = pointsfont.render(inputtext, True, (0, 0 ,0))
        screen.blit(textsurface, (int(displayWidth/2+85), int(displayHeight/2 + 58)))

try: 
    winScore = int(inputtext)
except ValueError:
    winScore = 10
         
# main game loop

while not gameOver:

    # general game controls and block movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not ball_moving:
                    ball_moving = True
                    counter_changex = int((math.cos(angle*math.pi/180)*speed))
                    counter_changey = int((math.sin(angle*math.pi/180)*speed))
            if event.key == pygame.K_UP:
                yPos2_change = -10     
            if event.key == pygame.K_DOWN:
                yPos2_change = 10
            if event.key == pygame.K_w:
                yPos1_change = -10
            if event.key == pygame.K_s:
                yPos1_change = 10
            if event.key == pygame.K_ESCAPE:
                gameOver = True
                print(); 
                print("Bye!"); 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yPos2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                yPos1_change = 0
    if yPos1 < 0 and yPos1_change < 0:
        yPos1_change = 0
    if yPos2 < 0 and yPos2_change < 0:
        yPos2_change = 0
    if yPos1 > displayHeight - blockLength and yPos1_change > 0:
        yPos1_change = 0
    if yPos2 > displayHeight - blockLength and yPos2_change > 0:
        yPos2_change = 0                     
    yPos1 += yPos1_change
    yPos2 += yPos2_change
  
    screen.fill(pygame.Color('papayawhip'))
    
    # update and render blocks
    block1.y = yPos1
    block1.render()
    block1.rect.topleft = (0, yPos1)

    block2.y = yPos2
    block2.render()
    block2.rect.topleft = (610, yPos2)
    
    #update and render ball 
    ball.x += counter_changex
    ball.y += counter_changey
    ball.render()
    ball.rect.topleft = (ball.x,ball.y)

    #update and render score
    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 25)
    text1 = myfont.render("Player 1: " + str(score1), 1, blockColor1)
    screen.blit(text1, (50, 50))
    text2 = myfont.render("Player 2: " + str(score2) , 1, blockColor2)
    screen.blit(text2, (displayWidth -150, 50))
    
    #collision detection for ball
    if ball.y <= 0 or ball.y+40 >= 480:
        if angle >= 135 and angle <= 225:
            angle = 360-angle
        else:
            angle = -angle 
        counter_changex = int((math.cos(angle*math.pi/180)*speed))
        counter_changey = int((math.sin(angle*math.pi/180)*speed))
        
    if ball.x <= -40:
        score2 += 1
        if score2 >= winScore:
            winner = True
            gameOver = True
        restart()        
    elif ball.x+40 >= 680:
        score1+=1
        if score1 >= winScore:
            winner = True
            gameOver = True
        restart()
        
    if pygame.sprite.collide_rect(block1, ball):
        print("block1")
        print(angle)
        if ball.x >= blockWidth - speed - 1:
            newAngle = 180 - angle 
            if newAngle >= 0:
                newAngle = newAngle + (45-newAngle)*((ball.y + 20) - (block1.y + 35))/55
            elif newAngle < 0:
                newAngle = newAngle + (-45-newAngle)*((block1.y + 35) - (ball.y + 20))/55
            if speed < MAXSPEED:
                speed += 0.5
            angle = newAngle 
            print(angle)
            counter_changex = int((math.cos(angle*math.pi/180)*speed))
            counter_changey = int((math.sin(angle*math.pi/180)*speed))
        
    if pygame.sprite.collide_rect(ball, block2):
        print("block2")
        print(angle)
        if ball.x+40 <= 640 - (blockWidth - speed - 1):
            newAngle = 180 - angle 
            if newAngle <= 180:
                newAngle = newAngle + (135-newAngle)*((ball.y + 20) - (block2.y + 35))/55
            elif newAngle > 0:
                newAngle = newAngle + (225-newAngle)*((block2.y + 35) - (ball.y + 20))/55
            if speed < MAXSPEED:
                speed += 0.5
            angle = newAngle 
            print(angle)
            counter_changex = int((math.cos(angle*math.pi/180)*speed))
            counter_changey = int((math.sin(angle*math.pi/180)*speed))
        
    pygame.display.flip()

    clock.tick(60)


# winner display

while winner:
        pygame.display.flip()
        screen.fill(pygame.Color('azure2'))
        myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 100)
        if score1 > score2:
            color = blockColor1
            text1 = myfont.render("Player 1", 1, color)
        if score2 > score1:
            color = blockColor2
            text1 = myfont.render("Player 2", 1, color)
        screen.blit(text1, (int(displayWidth/2-135), int(displayHeight*0.2)))
        text2 = myfont.render("YOU WIN!", 1, color)
        screen.blit(text2, (int(displayWidth/2-170), int(displayHeight*0.2+80)))

        myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 30)
        scoretext = myfont.render("Player 1: " + str(score1) + "              Player 2: " + str(score2), 1, color)
        screen.blit(scoretext, (int(displayWidth/2-150), int(displayHeight*0.2 + 180)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    winner = False


pygame.quit()
quit()

