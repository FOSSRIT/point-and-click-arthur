import pygame, random, sys
import os
from pygame.locals import *
from random import randint

WINDOWWIDTH = 1200
WINDOWHEIGHT = 900

class Everything:
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT));
    def __init__(self):
	pygame.init()
	mainClock = pygame.time.Clock()
	pygame.display.set_caption('Point And Prototype')
	pygame.mouse.set_visible(False)

    def update(self):
        game.update()       
	gui.update()
	bkgrnd.update()
	graphics.update()
	pygame.display.update()

class myMouse:
    customCursor = pygame.image
    oldX = 0
    oldY = 0
    def __init__(self):
	print ("Building mouse")
        self.customCursor = pygame.image.load("mousecursor.png")
        everything.windowSurface.blit(self.customCursor,(0,0))
    def update (self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mX,mY = event.pos
		self.oldX = mX
                self.oldY = mY
	everything.windowSurface.blit(self.customCursor,(self.oldX,self.oldY))	

class GUI:
    def __init__(self):
	print("made GUI!")
    def update(self):
        '''
        print("update GUI")
        '''
class Graphics:
    customMouse = object
    allSprites = []
    def __init__(self):
        self.customMouse = myMouse()
        self.load_all_sprites()

    def update(self):
        for arrays in self.allSprites:
            for sprites in arrays:
                sprites.location = (sprites.x, sprites.y,100)
		if (sprites.name == "Walking"):
                    sprites.x += 3                    
                sprites.render(everything.windowSurface)
	self.customMouse.update()

    def load_all_sprites(self):
        self.allSprites.append(self.compileImages(72, 104, 'walktest.png', 20, False, 0, 200,100,"Walking"))
        self.allSprites.append(self.compileImages(48, 48, 'birdsprite.png', 20, True, 1, 300,100,"Dove"))

    def load_sliced_sprites(self,w, h, filename):
        images = []
        master_image = pygame.image.load(os.path.join('', filename)).convert_alpha()

        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width/w)):
    	    images.append(master_image.subsurface((i*w,0,w,h)))
        return images

    def compileImages (self, tileX, tileY, str, fps, loopStart, startFrame, spriteX, spriteY, name):
        tempSprite = self.load_sliced_sprites(tileX, tileY, str)
        sprites = []
        sprites.append(AnimatedSprite(tempSprite, fps, loopStart, startFrame, spriteX, spriteY, name, tileX, tileY))
        return sprites

class AnimatedSprite(pygame.sprite.Sprite):
    idle = False
    visible = True
    myStartSprite = 0
    x = 0
    y = 0
    name = "nope"
    rectangle = pygame.rect
    height = 0
    width = 0
    def __init__(self, images, fps, idleTag, startSprite, locX, locY, spriteName, w, h):
        self.name = spriteName
        self.height = h
        self.width = w
        self.rectangle = pygame.draw.rect(everything.windowSurface,0,(self.x,self.y, w, h))
        self.x = locX
        self.y = locY
        self.idle = idleTag
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        self._start = pygame.time.get_ticks()
        self._delay = 3000 / fps
        self._last_update = 0
        self._frame = startSprite
        self.myStartSprite = startSprite
        
        self.update(pygame.time.get_ticks())

    def update(self, t):
        if t - self._last_update > self._delay:
            if (self.idle == False): #when hovered over
                self._frame += 1
                if self._frame >= len(self._images):
                    self._frame = self.myStartSprite
                
            if (self.idle == True):
                self._frame = 0 #idle. Could probably edit this slightly and make an idle animation
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
        self.update(pygame.time.get_ticks())
	if (self.visible == True):
            self.rectangle.move(self.x,self.y)
            everything.windowSurface.blit(self.image, (self.x, self.y))

class Bkgrnd:
    image = pygame.image
    def __init__(self,str):
	print("made Bkgrnd!")
	self.image = pygame.image.load(str)	
        everything.windowSurface.blit(self.image,(0,0))

    def update(self):
	everything.windowSurface.blit(self.image,(0,0))
        '''
	//image render
	'''
    def bkgrndImage(self,str):
        pygame.image.load(str)

	'''
	//animations not 4 game
	'''

class mouseEventHandler(pygame.Rect):
    myRect = pygame.rect
    def __init__(self, mouseX, mouseY):
	self.myRect = pygame.draw.rect(everything.windowSurface,0,(mouseX,mouseY,5,5))
    def click(self, tempRect):
	print "mouseEvent fired!"
	if self.myRect.colliderect(tempRect):
	    return True

class Game:
    endGame = False
    
    def __init__(self):
        print("made Game!")
        
    def update(self):
        if (Game.endGame ==False):
            for arrays in graphics.allSprites:
                for sprites in arrays:
                    if (sprites.name == "Dove"):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
			        mX,mY = event.pos
			        mouseRect = mouseEventHandler(mX,mY)
			        if mouseRect.click(sprites.rectangle):
				    print("hitMouse!")
                            if event.type == QUIT:
                                Game.endGame = True
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Game.endGame = True
        '''
        //mouse position
        //check for
            //clickable things clicked
            //rendering animations
        //Logic for
            //Game
            //saving(later)
            //input
        '''
everything = Everything()
game = Game()        
bkgrnd = Bkgrnd(str="kingarthur.png")
graphics = Graphics()
gui = GUI()
while True:
   everything.update()
