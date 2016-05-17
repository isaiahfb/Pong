
import pygame
import sys

pygame.init()

displayWidth = 640
displayHeight = 480

#print(pygame.font.get_fonts());

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

screen = pygame.display.set_mode((displayWidth,displayHeight))

x = (displayWidth*0.45)
y = (displayHeight*0.8)

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
winScore = input("How many points do you want to play to? ")

gameOver = False
winnner = False


blockWidth = 15
blockLength = 70
yPos1 = displayHeight/2-blockLength/2
yPos2 = displayHeight/2-blockLength/2

class StartButton:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 124
        self.height = 50
        self.rect = pygame.Rect(x,y,self.width,self.height)
    def render(self):
        pygame.draw.rect(screen,pygame.Color('red'),(self.x,self.y,self.width,self.height))

button = StartButton(displayWidth/2-62, displayHeight*0.4)
play = False


while not play:
    clock.tick(60)
    pygame.display.flip()
    screen.fill(pygame.Color('black'))
    button.render()
    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 80)
    text = myfont.render("PLAY", 1, (0, 0, 0))
    screen.blit(text, (displayWidth/2-62,displayHeight*0.4))
    
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

                
while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameOver = True
                print(); 
                print(":^) Bye! :^)");
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and yPos2+blockLength <= displayHeight:
        yPos2+=10
    if keys[pygame.K_UP] and yPos2 >= 0:
        yPos2-=10
    if keys[pygame.K_s] and yPos1+blockLength <= displayHeight:
        yPos1+=10
    if keys[pygame.K_w] and yPos1 >= 0:
        yPos1-=10
        
    
    
    screen.fill(pygame.Color('papayawhip'))

    pygame.draw.circle(screen, pygame.Color('salmon'), (320,250), 20, 0)  
    block1 = pygame.Surface((blockWidth,blockLength))
    block1.fill(pygame.Color('royalblue1'))
    block2 = pygame.Surface((blockWidth,blockLength))
    block2.fill(pygame.Color('royalblue1'))
    screen.blit(block1,(0, yPos1))
    screen.blit(block2, (625, yPos2))
    
    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 20)
    text = myfont.render("HI SAIAH!", 1, (154, 12, 63))
    screen.blit(text, (180, 180))
    
    pygame.display.flip()

    clock.tick(60)
    
while winner:
        pygame.display.flip()
        screen.fill(pygame.Color('azure2'))
        myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 100)
        if score1 > score2:
            color = player1Color
            text1 = myfont.render("Player 1,", 1, color)
        if score2 > score1:
            color = playerr2Color
            text1 = myfont.render("Player 2,", 1, color)
        screen.blit(text1, (displayerWidth/2-100, displayHeight*0.3))
        text2 = myfont.render("YOU WIN", 1, color)
        screen.blit(text2, (displayWidth/2-100, displayHeight*0.3+100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winnner = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    winner = False
                    print(); 
                    print(":^) Bye! :^)");
pygame.quit()
quit()
