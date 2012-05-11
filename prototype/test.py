'''
Issues:
mouseRect issues for gui.rollover
'''
import pygame, random, sys
import os
from pygame.locals import *
from random import randint

WINDOWWIDTH = 1200
WINDOWHEIGHT = 900


class Everything:
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    font = pygame.font
    TEXTCOLOR = (255, 255, 255)
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)
        mainClock = pygame.time.Clock()
        pygame.display.set_caption('Point And Prototype')
        pygame.mouse.set_visible(True)

    def drawText(self, text, font, surface, x, y):
        textobj = font.render(text, 1, everything.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def update(self):
        gui.update()
        bkgrnd.update()
        game.update()
        pygame.display.update()

class GUI:
    rollover = False
    displayText = False
    inventory = pygame.rect
    def __init__(self):
        print("made GUI!")
        savebox = pygame.draw.rect(everything.windowSurface,(255,255,0),(1100,0,100,50))
        savetext = everything.drawText("Save",everything.font,everything.windowSurface,1110,10)
        #Current issue: Rect doesnt show up, but is irrelevant when the GUI becomes sprite based
        self.inventory = pygame.draw.rect(everything.windowSurface,(255,255,0),(300, 1000,700,180))
    def update(self):
        if(gui.rollover == True):
            everything.drawText("Inventory",everything.font, everything.windowSurface,300,780) 
            self.inventory=self.inventory.move(300,820)
        elif(gui.rollover == False):
            self.inventory=self.inventory.move(300,1000)
        if(gui.displayText == True):
            textBox = pygame.draw.rect(everything.windowSurface,(255,255,0),(300,0,700,100))
            everything.drawText("King Arthur: \"Welcome to my Game!\"",everything.font, everything.windowSurface,310,10) 
        elif(gui.displayText == False):
            textBox = pygame.draw.rect(everything.windowSurface,(255,255,0),(300,0,0,0))
        '''
        //save button update
        //invetory render
            //items in invetory redoer
        //text render
        '''

class Bkgrnd:
    def __init__(self,str):
        print("made Bkgrnd!")
        image= pygame.image.load(str)
        everything.windowSurface.blit(image,(0,0))
    def update(self):
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
        tempRect = pygame.draw.rect(everything.windowSurface,0,(mouseX,mouseY,1,1))
    def click(self, tempRect):
        print "mouseEvent fired!"
        if tempRect.colliderect(tempRect):
            return True;

class Game:
    endGame = False
    
    def __init__(self):
        print("made Game!")
        
    def update(self):
        testRect = pygame.draw.rect(everything.windowSurface,0,(300,100,20,20))
        if (Game.endGame ==False):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mX,mY = event.pos
                    mouseRect = pygame.draw.rect(everything.windowSurface,(0,0,0),(mX,mY,1,1))
                    if(mouseRect.y >700):
                        gui.rollover = True
                    if(mouseRect.y <700):
                        gui.rollover = False
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
                    mX,mY = event.pos
                    mouseRect = mouseEventHandler(mX,mY)
                    if mouseRect.click(testRect):
                        print("hitMouse!")
                        gui.displayText = True
                if event.type == QUIT:
                    Game.endGame = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Game.endGame = True
        elif (Game.endGame ==True):
            pygame.quit()
            
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
bkgrnd = Bkgrnd(str="kingarthur.png")
game = Game()
gui = GUI()
while True:
    everything.update()
