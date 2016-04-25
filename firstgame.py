import pygame
import sys

pygame.init()

display_width = 640
display_height = 480
number = 20
#just testing
mysteryColor = (30, 25, 111)
mysteryColorAgain = (21, 120, 255)
mysteryColorMeUp = (130, 52, 201)
red = pygame.Color('red')

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width,display_height))

starX = 100
starY = 100
star = pygame.image.load('star.png')
print(star.get_rect().size)
star = pygame.transform.scale(star, (100,100))

x = (display_width*0.45)
y = (display_height*0.8)

gameOver = False

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
 
    print(event)
    
    screen.fill(mysteryColor)
    
    pygame.draw.circle(screen, pygame.Color('chartreuse3'), (320,250), 20, 0)
    pygame.draw.rect(screen, mysteryColorMeUp, (0,0,15,70), 0)
    pygame.draw.rect(screen, mysteryColorMeUp, (625,0,15,70), 0)

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]:
        pygame.draw.circle(screen, pygame.Color('black'), (500,300), number, 0)
        number+=1
    if keys[pygame.K_DOWN]:
        print("DOWN");
    if keys[pygame.K_a]:
        starX-=2
        
    if keys[pygame.K_d]:
        starX+=2
    if keys[pygame.K_w]:
        starY-=2
    if keys[pygame.K_s]:
        starY+=2
    
    
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('Hiiiiiiiii', True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    screen.blit(text, [300,50])

    screen.blit(star, (starX,starY))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
