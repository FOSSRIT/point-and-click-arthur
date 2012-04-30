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

CurrentDoveX = 1035 #used to control movement of animation
CurrentDoveY = 450
KnightX = 100

startUp = False
doveHover = False
endGame = False
textclicked = False
imageclicked = False
soundclicked = False
animclicked = False



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

class AnimatedDove(pygame.sprite.Sprite):
    def __init__(self, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        self._start = pygame.time.get_ticks()
        self._delay = 3000 / fps
        self._last_update = 0
        self._frame = 0
        
        self.update(pygame.time.get_ticks())

    def update(self, t):

        if t - self._last_update > self._delay:
            if (doveHover == True): #when hovered over
                self._frame += 1
                if self._frame >= len(self._images):
                    self._frame = 1 #Does not loop at frame 0! Starts at second frame because frame 0 is idle
                
            if (doveHover == False):
                self._frame = 0 #idle. Could probably edit this slightly and make an idle animation
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
            self.update(pygame.time.get_ticks())
            windowSurface.blit(self.image, self.location)

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 2000 / fps
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

#code for background image, add all other backgrounds here (load them all at once)
background1 = pygame.image.load("kingarthur.png")
size = (width, height) = background1.get_size()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont(None, 48)

#drawText('Our Prototype', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
#drawText('Press Any Key To Start', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)

startUp = True
backgroundRect = background1.get_rect()

# sprite data. Every sprite needs to load_spliced_sprites and then added to its own array
start_dove = load_sliced_sprites(48, 48, 'birdsprite.png')
doveSprites = []
doveSprites.append(AnimatedDove(start_dove, 15))

arthur_images = load_sliced_sprites(72, 104, 'walktest.png')
sprites	= []
sprites.append(AnimatedSprite(arthur_images, 15))

mouseRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(0,0,1,1))
doveRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(CurrentDoveX,CurrentDoveY,48,48))

while (startUp == True):
                
    if(endGame == False):
        screen.blit(background1, backgroundRect)
        for sprite in doveSprites:
            sprite.location = (CurrentDoveX,CurrentDoveY)
            sprite.render(windowSurface)
        for event in pygame.event.get():
            if event.type == KEYDOWN: #moves to next screen when any button is pressed
                startUp = False
            if event.type == QUIT: #fixes crashing at exit on this screen
                endGame = True
                pygame.quit()
            if event.type == pygame.MOUSEMOTION: # hover over bird
                mX,mY = event.pos
                mouseRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(mX,mY,1,1))
                if mouseRect.colliderect(doveRect): #draws a "hitbox" for the bird and checks to see if the mouse collides with it
                    doveHover = True
            if event.type == pygame.MOUSEBUTTONDOWN: #moves to next screen on click
                startUp = False
        if (doveHover == True): #moves the dove's position
            CurrentDoveX -= 5
            CurrentDoveY -= 1
                
        pygame.display.update()

while (endGame ==False):
    windowSurface.fill(BACKGROUNDCOLOR)
    makeText = pygame.draw.rect(windowSurface,BLUE,(400,100,20,20))
    makeImage = pygame.draw.rect(windowSurface,GREEN,(350,100,20,20))
    makeAnim = pygame.draw.rect(windowSurface,RED,(300,100,20,20))
    #makeSound = pygame.draw.rect(windowSurface,WHITE,(450,100,20,20))
    mouseRect = pygame.draw.rect(windowSurface,BACKGROUNDCOLOR,(0,0,1,1))
    
    if textclicked == False:
        drawText('Point And Prototype', font, windowSurface,300,300)
    elif textclicked == True:
        drawText('you clicked the blue button!', font, windowSurface,300,300)

    if imageclicked == True:
        windowSurface.blit(image, (400,200))

    #if soundclicked == True:
        #pygame.mixer.Sound("sound.wav").play()
    #elif soundclicked == False: had some problems with this code during testing, was causing crashes, commented it out for now
        # pygame.mixer.stop()
    if animclicked == True:
        for sprite in sprites:
            sprite.location = (KnightX,800)
            sprite.render(windowSurface)
    
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
            if textclicked == False:
                textclicked = True
        if mouseRect.colliderect(makeImage):
            if imageclicked == True:
                imageclicked = False
            if imageclicked == False:
                imageclicked = True
        #if mouseRect.colliderect(makeSound):
            #if soundclicked == True:
               #soundclicked = False
            #elif soundclicked == False:
                #soundclicked = True
        if mouseRect.colliderect(makeAnim):
            if animclicked == True:
                animclicked = False
            if animclicked == False:
                animclicked = True
    
    pygame.display.update()

if(endGame == True):
    pygame.quit()
