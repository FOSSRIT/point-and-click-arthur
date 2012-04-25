import pygame, random, sys
import os
from pygame.locals import *
from random import randint

WINDOWWIDTH = 900
WINDOWHEIGHT = 500
RESOLUTION = (WINDOWWIDTH, WINDOWHEIGHT)

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

def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    '''
    images = []
    master_image = pygame.image.load(os.path.join('', filename)).convert_alpha()

    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0

        # Call update to set our first image.
        self.update(pygame.time.get_ticks())

    def update(self, t):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.

        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
            self.update(pygame.time.get_ticks())
            windowSurface.blit(self.image, self.location)

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
arthur_images = load_sliced_sprites(16, 34, 'animation.png')
sprites	= []
sprites.append(AnimatedSprite(arthur_images, 15))



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

    if animclicked == True:
        for sprite in sprites:
            sprite.location = (100,100)
            sprite.render(windowSurface)
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

if(endGame == True):
    pygame.quit()
