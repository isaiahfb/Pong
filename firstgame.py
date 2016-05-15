
import pygame
import sys

pygame.init()

display_width = 640
display_height = 480

#print(pygame.font.get_fonts());

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width,display_height))

x = (display_width*0.45)
y = (display_height*0.8)

print("NOTES:");
print();
print("PLAYER ONE: (Left) ");
print("Press 'w' to move up, 's' to move down");
print("PLAYER TWO: (Right) ");
print("Press 'Up' to move up, 'Down' to move down");
print();
print("Press 'esc' to exit!"); 

gameOver = False

yPos1 = 0
yPos2 = 0
yPos1_change = 0;
yPos2_change = 0; 

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
  
    screen.fill(pygame.Color('papayawhip'))

    pygame.draw.circle(screen, pygame.Color('salmon'), (320,250), 20, 0)  
    block1 = pygame.draw.rect(screen, pygame.Color('royalblue1'), (0,yPos1,15,70), 0)
    block2 = pygame.draw.rect(screen, pygame.Color('royalblue1'), (625,yPos2,15,70), 0)   

    myfont = pygame.font.SysFont("batangbatangchegungsuhgungsuhche", 20)
    text = myfont.render("HI SAIAH!", 1, (154, 12, 63))
    screen.blit(text, (180, 180))
    
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
