import pygame
import sys
import random
import math

pygame.init()

displayWidth = 640
displayHeight = 480

#print(pygame.font.get_fonts());

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

screen = pygame.display.set_mode((displayWidth,displayHeight))

#x = (displayWidth*0.45)
#y = (displayHeight*0.8)

print("NOTES:");
print();
print("PLAYER ONE: (Left) ");
print("Press 'w' to move up, 's' to move down");
print("PLAYER TWO: (Right) ");
print("Press 'Up' to move up, 'Down' to move down");
print();
print("Press 'esc' to exit!");
print();
print();
talk = input("How many points do you want to play to? ")
winScore = int(talk)

gameOver = False
winner = False

blockWidth = 15
blockLength = 70
blockColor1 = pygame.Color('royalblue1')
blockColor2 = pygame.Color('mediumspringgreen')
yPos1 = (displayHeight/2)-(blockLength/2)
yPos2 = (displayHeight/2)-(blockLength/2)
yPos1_change = 0
yPos2_change = 0
counterx = 0
countery = 0
counter_changex = 0
counter_changey = 0
speed = 7
score1 = 0
score2 = 0

class StartButton:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 250
        self.height = 80
        self.rect = pygame.Rect(x,y,self.width,self.height)
    def render(self):
        pygame.draw.rect(screen,pygame.Color('lightsalmon'),(self.x,self.y,self.width,self.height))

button = StartButton(displayWidth/2-110, displayHeight*0.4)
play = False

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

def restart():
    angle1 = random.randint(134, 225)
    angle2 = random.randint(-46,45)
    angleChoose = random.randint(0,1)
    if angleChoose == 0:
        global angle
        angle = angle1
        global counter_changex
        counter_changex = (math.cos(angle*math.pi/180)*speed)
        global counter_changey
        counter_changey = (math.sin(angle*math.pi/180)*speed)
    if angleChoose == 1:
        global angle
        angle = angle2
        global counter_changex
        counter_changex = (math.cos(angle*math.pi/180)*speed)
        global counter_changey
        counter_changey = (math.sin(angle*math.pi/180)*speed) 

while not play:
    clock.tick(60)
    pygame.display.flip()
    screen.fill(pygame.Color('paleturquoise2'))
    button.render()
    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 80)
    text = myfont.render("PLAY", 1, (255, 255, 255))
    screen.blit(text, (displayWidth/2-95,displayHeight*0.4))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
            gameOver = True
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_ESCAPE:
                play = True
                gameOver = True
                print(); 
                print(":^) Bye! :^)");
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if button.rect.collidepoint(pos):               
                play = True
                restart()
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and yPos2+blockLength <= displayHeight:
        yPos2+=10
    if keys[pygame.K_UP] and yPos2 >= 0:
        yPos2-=10
    if keys[pygame.K_s] and yPos1+blockLength <= displayHeight:
        yPos1+=10
    if keys[pygame.K_w] and yPos1 >= 0:
        yPos1-=10
                
while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
            
        if event.type == pygame.KEYDOWN:
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
                print(":^) Bye! :^)"); 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yPos2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                yPos1_change = 0
                
    yPos1 += yPos1_change
    yPos2 += yPos2_change
    counterx += counter_changex
    countery += counter_changey
  
    screen.fill(pygame.Color('papayawhip'))

    #image = pygame.draw.circle(screen, pygame.Color('salmon'), (320,250), 20, 0)
    beachBall = pygame.image.load('circle.png')
    image = pygame.transform.scale(beachBall, (40,40))
 
    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 20)
    text = myfont.render("HI SAIAH!", 1, (154, 12, 63))
    screen.blit(text, (180, 180))

    block1 = Block(blockColor1, 0, yPos1, blockWidth, blockLength)
    block1.render()
    #block1 = pygame.Surface((blockWidth,blockLength))
    #block1.fill(pygame.Color('royalblue1'))
    block1.rect.topleft = (0, yPos1)
    
    block2 = Block(blockColor2, 625, yPos2, blockWidth, blockLength)
    block2.render()
    #block2 = pygame.Surface((blockWidth,blockLength))
    #block2.fill(pygame.Color('royalblue1'))
    block2.rect.topleft = (625, yPos2)

    #screen.blit(block1,(0, yPos1))
    #screen.blit(block2, (625, yPos2))
    
    ball = Circle(image, 320, 250)
    ball.x += counterx
    ball.y += countery
    ball.render()
    ball.rect.topleft = (ball.x,ball.y)
    
    if ball.y <= 0 or ball.y+40 >= 480:
        angle = angle*-1
        counter_changex = (math.cos(angle*math.pi/180)*speed)
        counter_changey = (math.sin(angle*math.pi/180)*speed)
        
    if ball.x <= 0:
        print("Player 2 gets a point");
        counterx = 0
        countery = 0
        score2 += 1
        if score2 >= winScore:
            winner = True
        restart()        
    elif ball.x+40 >= 640:
        print("Player 1 gets a point");
        counterx = 0
        countery = 0
        score1+=1
        if score1 >= winScore:
            winner = True
        restart()
        
    if pygame.sprite.collide_rect(block1, ball):
        print("p.1 blocked");
        if angle > 0:
            angle = 180-angle
        elif angle < 0:
            angle = (180+angle)*-1
        counter_changex = (math.cos(angle*math.pi/180)*speed)
        counter_changey = (math.sin(angle*math.pi/180)*speed)
        
    if pygame.sprite.collide_rect(ball, block2):
        print("p.2 blocked");
        if angle > 0:
            angle = 180-angle
        elif angle < 0:
            angle = (180+angle)*-1
        counter_changex = (math.cos(angle*math.pi/180)*speed)
        counter_changey = (math.sin(angle*math.pi/180)*speed)
        
    pygame.display.flip()

    clock.tick(60)

while winner:
        pygame.display.flip()
        screen.fill(pygame.Color('azure2'))
        myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 100)
        if score1 > score2:
            color = blockColor1
            text1 = myfont.render("Player 1,", 1, color)
        if score2 > score1:
            color = blockColor2
            text1 = myfont.render("Player 2,", 1, color)
        screen.blit(text1, (displayWidth/2-200, displayHeight*0.3))
        text2 = myfont.render("YOU WIN", 1, color)
        screen.blit(text2, (displayWidth/2-220, displayHeight*0.3+100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    winner = False
                    print(); 
                    print(":^) Bye! :^)");

pygame.quit()
quit()

