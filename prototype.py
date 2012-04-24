import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 1200
WINDOWHEIGHT = 900

TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

endGame = False
textclicked = False
imageclicked = False
soundclicked = False
animclicked = False

if(endGame == True):
    pygame.quit()
    sys.exit()
	
	
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                endGame = true
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    endGame = true
                return
				
				
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
	
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Point And Prototype')
pygame.mouse.set_visible(True)
image = pygame.image.load("image.png")

font = pygame.font.SysFont(None, 48)

drawText('Our Prototype', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press Any Key To Start', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

while (endGame ==False):
    windowSurface.fill(BACKGROUNDCOLOR)
    makeText = pygame.draw.rect(windowSurface,BLUE,(400,100,20,20))
    makeImage = pygame.draw.rect(windowSurface,GREEN,(350,100,20,20))
    makeAnim = pygame.draw.rect(windowSurface,RED,(300,100,20,20))
    makeSound = pygame.draw.rect(windowSurface,WHITE,(450,100,20,20))
    mouseRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(0,0,1,1))
    
    if textclicked == False:
        drawText('Point And Prototype', font, windowSurface,300,300)
    elif textclicked == True:
        drawText('you clicked the blue button!', font, windowSurface,300,300)

    if imageclicked == True:
        windowSurface.blit(image, (400,200))

    if soundclicked == True:
        pygame.mixer.Sound("sound.wav").play()
    elif soundclicked == False:
        pygame.mixer.stop()

    #if animclicked == True:
        #code to run animation
    #elif animclicked == False:
        #code to stop animation
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mX,mY = event.pos
            mouseRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(mX,mY,1,1))
        if event.type == QUIT:
            endGame = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                endGame = True;
        if mouseRect.colliderect(makeText):
            if textclicked == True:
                textclicked = False
            elif textclicked == False:
                textclicked = True
        if mouseRect.colliderect(makeImage):
            if imageclicked == True:
                imageclicked = False
            elif imageclicked == False:
                imageclicked = True
        if mouseRect.colliderect(makeSound):
            if soundclicked == True:
                soundclicked = False
            elif soundclicked == False:
                soundclicked = True
        if mouseRect.colliderect(makeAnim):
            if animclicked == True:
                animclicked = False
            elif animclicked == False:
                animclicked = True
    
    pygame.display.update()
    

