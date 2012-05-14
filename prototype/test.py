import pygame, random, sys
import os
from pygame.locals import *
from random import randint

'''
Question from David (oddshocks):
When we write the final code, could we use variables like_this
rather than theseOnes? Variables like_this are more Python-y.
CapitalLetters are good for class names.
Just a thought, your guys' call. :)
'''

### CONSTANTS (also, these contants might be better named with underscores (_))
WINDOWWIDTH = 1200
WINDOWHEIGHT = 900
TEXTCOLOR = (255, 255, 255)

class Everything(object):
    def __init__(self):
        pygame.init() ### INITIALIZE PYGAME
        self.windowSurface = pygame.display.set_mode((WINDOWWIDTH,
            WINDOWHEIGHT))
        self.font = pygame.font
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)
        mainClock = pygame.time.Clock()
        pygame.display.set_caption('Point And Prototype')
        pygame.mouse.set_visible(False)

    def drawText(self, text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def update(self):
        game.update()       
        gui.update()
        bkgrnd.update()
        graphics.update()
        # pygame.display.update()
        # Pretty sure we should use flip() here?
        pygame.display.flip()

class myMouse(object):
    def __init__(self):
        self.customCursor = pygame.image
        self.oldX = 0
        self.oldY = 0
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

class GUI(object):
    def __init__(self):
        self.rollover = False
        self.displayText = False
        savebox = pygame.draw.rect(
            everything.windowSurface,(255,255,0),(1100,0,100,50))
        savetext = everything.drawText(
            "Save",everything.font,everything.windowSurface,1110,10)
        # Current issue: Rect doesnt show up,
        # but this becomes irrelevant when the GUI becomes sprite based
        # oddshocks: it is possible that I fixed this, not sure
        self.inventory = pygame.draw.rect(
            everything.windowSurface,(255,255,0),(300, 1000,700,180))
        print("made GUI!")
    def update(self):
        if(self.rollover == True):
            everything.drawText(
                "Inventory",everything.font, everything.windowSurface,300,780) 
            self.inventory=self.inventory.move(300,820)
        elif(self.rollover == False):
            self.inventory=self.inventory.move(300,1000)
        if(self.displayText == True):
            textBox = pygame.draw.rect(
                everything.windowSurface,(255,255,0),(300,0,700,100))
            everything.drawText(
                "King Arthur: \"Welcome to my Game!\"",everything.font,\
                everything.windowSurface,310,10) 
        elif(self.displayText == False):
            textBox = pygame.draw.rect(
                everything.windowSurface,(255,255,0),(300,0,0,0))
        # print("updated GUI")

class Graphics(object):
    def __init__(self):
        self.customMouse = myMouse()
        self.allSprites = []
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
        self.allSprites.append(self.compileImages(
            72, 104, 'walktest.png', 20, False, 0, 200,100,"Walking"))
        self.allSprites.append(self.compileImages(
            48, 48, 'birdsprite.png', 20, True, 1, 300,100,"Dove"))

    def load_sliced_sprites(self,w, h, filename):
        images = []
        master_image = pygame.image.load(
            os.path.join('', filename)).convert_alpha()
        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width/w)):
            images.append(master_image.subsurface((i*w,0,w,h)))
        return images

    def compileImages (self, tileX, tileY, str, fps,
        loopStart, startFrame, spriteX, spriteY, name):
        tempSprite = self.load_sliced_sprites(tileX, tileY, str)
        sprites = []
        sprites.append(
            AnimatedSprite(
                tempSprite, fps, loopStart, startFrame,\
                spriteX, spriteY, name, tileX, tileY))
        return sprites

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps, idleTag,\
        startSprite, locX, locY, spriteName, w, h):
        self.x = locX
        self.y = locY
        self.name = spriteName
        self.height = h
        self.width = w
        self.visible = True
        self.rectangle = pygame.draw.rect(
            everything.windowSurface,0,(self.x,self.y, w, h))
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
                self._frame = 0 # idle. 
                                # Could probably edit this slightly
                                # and make an idle animation
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
        self.update(pygame.time.get_ticks())
        if (self.visible == True):
            self.rectangle.move(self.x,self.y)
            everything.windowSurface.blit(self.image, (self.x, self.y))

class Bkgrnd(object):
    def __init__(self,str):
        print("made Bkgrnd!")
        self.image = pygame.image.load(str) 
        everything.windowSurface.blit(self.image,(0,0))

    def update(self):
        everything.windowSurface.blit(self.image,(0,0))
        # What are the next two comments for? -- David (oddshocks)
        '''
        //image render
        '''
    def bkgrndImage(self,str):
        pygame.image.load(str)

    '''
    //animations not 4 game
    '''

class mouseEventHandler(pygame.Rect):
    def __init__(self, mouseX, mouseY):
        self.myRect = pygame.draw.rect(
            everything.windowSurface,0,(
            mouseX,mouseY,5,5))
    def click(self, tempRect):
        print "mouseEvent fired!"
        if self.myRect.colliderect(tempRect):
            return True

class Game(object):
    def __init__(self):
        print("made Game!")
        self.endGame = False
        
    def update(self):
        if (self.endGame == False):
            for arrays in graphics.allSprites:
                for sprites in arrays:
                    if (sprites.name == "Dove"):
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEMOTION:
                                mX,mY = event.pos
                                mouseRect = pygame.draw.rect(
                                    everything.windowSurface,(0,0,0),(mX,mY,1,1))
                                if(mouseRect.y >700):
                                    gui.rollover = True
                                if(mouseRect.y <700):
                                    gui.rollover = False
                            if event.type == pygame.MOUSEBUTTONDOWN \
                                and pygame.mouse.get_pressed():
                                mX,mY = event.pos
                                mouseRect = mouseEventHandler(mX,mY)
                                if mouseRect.click(sprites.rectangle):
                                    print("hitMouse!")
                                    gui.displayText = True
                            if event.type == pygame.QUIT:
                                self.endGame = True
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    self.endGame = True
        else:
            quitting = True
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

quitting = False # is the game qutting?
clock = pygame.time.Clock()

### START THE GAME LOOP

while not quitting:
    clock.tick(30) # Set FPS to 30
    everything.update()

### END THE GAME LOOP

pygame.quit() # quit the game
