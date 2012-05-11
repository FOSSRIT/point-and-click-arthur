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
        pygame.mouse.set_visible(True)

    def update(self):
        bkgrnd.update()
        game.update()
        gui.update()
        pygame.display.update()

class GUI:
    def __init__(self):
        print("made GUI!")
    def update(self):
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

class Game:
    endGame = False
    
    def __init__(self):
        print("made Game!")
        
    def update(self):
        if (Game.endGame ==False):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mX,mY = event.pos
                    mouseRect = pygame.draw.rect(everything.windowSurface,(255,255,255),(mX,mY,1,1))
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
bkgrnd = Bkgrnd(str="kingarthur.PNG")
game = Game()
gui = GUI()
everything.update()
