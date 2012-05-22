import os
import pygame
import random
import sys
from pygame.locals import *
from random import randint

### CONSTANTS
WINDOW_WIDTH = 1028
WINDOW_HEIGHT = 768
TEXT_COLOR = (255, 255, 255)

'''
Sprite Names:
Dove
RedKnightWalk
GreenKnightWalk
BlueKnightWalk
MordredWalk
YellowKnightWalk
ArthurStand
MerlinMagic
ArthurWalk
Couldron
GreenKnight
MerlinMagic
GUIInventory
MerlinMagic
ArthurWalk
Couldron
GreenKnight
GUIInventory
GUIMapHit
GUISave
InventoryItems
InventoryWorld
MordredAttack
RedKnightStand
MerlinWalk
Monster

GrailWorld
WandWorld
DoveSingWorld
DoveWorld
SwordWorld

SwordInventory
SoupInventory
DoveInventory
DoveSingInventory
WandInventory
GrailInventory
BeltInventory
'''

class Everything(object):
    def __init__(self):
        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH,
            WINDOW_HEIGHT))
        self.font = pygame.font
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)
        pygame.display.set_caption('Point and Click Arthur')
        pygame.mouse.set_visible(False)

    def draw_text(self, text, font, surface, x, y):
        text_obj = font.render(text, 1, TEXT_COLOR)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def update(self):
        self.window_surface.fill((0,0,0))
        game.update()       
        background.update()
        for screens in screenArray:
            screens.update()
        gui.update()
        graphics.update()


class Screen(object):
    def __init__ (self, bg):
        self.fileName = bg
        self.sprites = []
        self.active = False
    def isActive(self):
        for screens in screenArray:
            screens.active = False
        background.background_image(str = self.fileName)
        self.active = True
    def update(self):
        if (self.active == True):
            for sprites in self.sprites:
                sprites.location = (sprites.x, sprites.y, 100)                
                sprites.render(everything.window_surface)
    def addSprite(self, sprite):
        #print "Loading " + sprite
        tempSprite = graphics.getSprite(sprite)
        self.sprites.append(tempSprite)

class MyMouse(object):
    def __init__(self):
        self.custom_cursor = pygame.image
        self.x = 0
        self.y = 0
        self.old_x = 0
        self.old_y = 0
        print 'Building mouse...' # Debug
        self.custom_cursor = pygame.image.load("mousecursor.png")
        everything.window_surface.blit(self.custom_cursor, (0, 0))
    def update (self):
        everything.window_surface.blit(self.custom_cursor,
            (self.old_x, self.old_y))  

class GUI(object):
    def __init__(self):
        self.rollover = False
        self.display_text = False
        save_text = everything.draw_text(
            "Save", everything.font,everything.window_surface, 1110, 10)
        # Current issue: Rect doesnt show up,
        # but this becomes irrelevant when the GUI becomes sprite based
        # oddshocks: it is possible that I fixed this, not sure
        self.InventorySprite = graphics.getSprite("GUIInventory")
        

    def update(self):
        if self.display_text == True:
            text_box = pygame.draw.rect(
                everything.window_surface, (255, 255, 0), (300, 0, 700, 100))
            everything.draw_text(
                "King Arthur: \"Welcome to my Game!\"", everything.font,
                everything.window_surface, 310, 10) 
        elif self.display_text == False:
            text_box = pygame.draw.rect(
                everything.window_surface, (255, 255, 0), (300, 0, 0, 0))
        self.InventorySprite.location = (100, 300, 100)                
        self.InventorySprite.render(everything.window_surface)

        graphics.getSprite("SwordInventory").render(everything.window_surface)
        if DoveClicked == True:
            graphics.getSprite("DoveInventory").render(everything.window_surface)
        graphics.getSprite("DoveSingInventory").render(everything.window_surface)
        graphics.getSprite("SoupInventory").render(everything.window_surface)
        graphics.getSprite("WandInventory").render(everything.window_surface)
        graphics.getSprite("GrailInventory").render(everything.window_surface)
        graphics.getSprite("BeltInventory").render(everything.window_surface)

        graphics.getSprite("Textbox").render(everything.window_surface)
        

        

class Graphics(object):
    def __init__(self):
        self.custom_mouse = MyMouse()
        self.all_sprites = []
        self.load_all_sprites()
    def update(self):
        self.custom_mouse.update()

    def load_all_sprites(self):
        #HUGE list of sprites being added. 
        self.all_sprites.append(self.compile_images(
            48, 48, 'birdsprite.png', 20, True, 0, 250, 315, "Dove"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALK.png', 20, True, 0, 200, 100, "RedKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKGREEN.png', 20, True, 0, 650, 540, "GreenKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKBLUE.png', 20, True, 0, 400, 560, "BlueKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKMORDRED.png', 20, True, 0, 200, 100, "MordredWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKYELLOW.png', 20, True, 0, 700, 560, "YellowKnightWalk"))
        self.all_sprites.append(self.compile_images(
            53, 97, 'arthurstand.png', 20, False, 0, 125, 565, "ArthurStand"))
        self.all_sprites.append(self.compile_images(
            124, 128, 'merlinMagic.png', 20, True, 0, 450, 400, "MerlinMagic"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'arthurWALK.png', 20, True, 0, 500, 500, "ArthurWalk"))
        self.all_sprites.append(self.compile_images(
            76, 72, 'couldron.png', 20, False, 0, 610, 325, "Couldron"))
        self.all_sprites.append(self.compile_images(
            60, 100, 'greenknight.png', 20, False, 0, 600, 550, "GreenKnight"))
        self.all_sprites.append(self.compile_images(
            100, 50, 'GUISave.png', 20, False, 0, 500, 500, "GUISave"))
        self.all_sprites.append(self.compile_images(
            126, 120, 'itemsINVENTORY.png', 20, False, 0, 500, 500, "InventoryItems"))
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, True, 0, 800, 550, "SwordWorld"))
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, True, 2, 700, 150, "DoveWorld"))
        self.getSprite("DoveWorld").my_start_sprite = 2
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, True, 3, 900, 200, "DoveSingWorld"))
        self.getSprite("DoveSingWorld").my_start_sprite = 3
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, True, 4, 500, 500, "WandWorld"))
        self.getSprite("WandWorld").my_start_sprite = 4
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, True, 5, 900, 50, "GrailWorld"))
        self.getSprite("GrailWorld").my_start_sprite = 5
        self.all_sprites.append(self.compile_images(
            100, 132, 'knight-attackMORDRED.png', 20, True, 0, 645, 555, "MordredAttack"))
        self.all_sprites.append(self.compile_images(
            60, 96, 'knightstand.png', 20, False, 0, 525, 520, "RedKnightStand"))
        self.all_sprites.append(self.compile_images(
            76, 120, 'merlinWALK.png', 20, False, 0, 500, 500, "MerlinWalk"))
        self.all_sprites.append(self.compile_images(
            96, 120, 'monster.png', 20, True, 0, 700, 555, "Monster"))
        
        #AJ: The following are the icons for the inventory GUI. You'll need to position them accordingly. You can either do it here, or use animated Sprite move function to place them correctly later in the code
        #To change it now, edit the numbers after the 0, that's the x and y of the sprites
        
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 650, "SwordInventory"))
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 650, "SoupInventory"))
        self.getSprite("SoupInventory").my_start_sprite = 1
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 650, "DoveInventory"))
        self.getSprite("DoveInventory").my_start_sprite = 2
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 500, "DoveSingInventory"))
        self.getSprite("DoveSingInventory").my_start_sprite = 3
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 500, "WandInventory"))
        self.getSprite("WandInventory").my_start_sprite = 4
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 500, "GrailInventory"))
        self.getSprite("GrailInventory").my_start_sprite = 5
        self.all_sprites.append(self.compile_images(
            125, 120, 'itemsINVENTORY.png', 20, True, 0, 500, 500, "BeltInventory"))
        self.getSprite("BeltInventory").my_start_sprite = 6

        #GUI Hit boxes, these are to move around the map. For children it's better to leave them visible, some turn visible only when the path opens
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 925, 400, "GUIMapHitForest1"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 950, 700, "GUIMapHitForest2"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 50, 700, "GUIMapHitForest3"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 350, 500, "GUIMapHitGawain1"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 900, 500, "GUIMapHitGawain2"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 25, 700, "GUIMapHitLancelot"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 925, 275, "GUIMapHitShack"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 175, 270, "GUIMapHitCastleInside1"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 900, 700, "GUIMapHitCastleInside2"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 350, 335, "GUIMapHitClearing1"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 900, 500, "GUIMapHitClearing2"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 25, 700, "GUIMapHitClearing3"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 900, 700, "GUIMapHitKeep"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 900, 700, "GUIMapHitAgravain"))

        self.all_sprites.append(self.compile_images(
            700, 180, 'GUIInventory.png', 20, False, 0, 175, 650, "GUIInventory"))
        self.all_sprites.append(self.compile_images(
            700, 180, 'GUIInventory.png', 20, False, 0, 175, -50, "Textbox"))
 

 
    def getSprite(self, sprite):
        #print "Looking for " + sprite
        for arrays in self.all_sprites:
            for sprites in arrays:
                #print "Sprites: Looking at " + sprites.name + " Comparing it to " + sprite
                if sprites.name == sprite:
                    #print "Found sprite!"
                    return sprites
        print "Error, could not find sprite by name"

    def load_sliced_sprites(self, w, h, file_name):
        images = []
        master_image = pygame.image.load(
            os.path.join('sprites/sheets/', file_name)).convert_alpha()
        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width / w)):
            images.append(master_image.subsurface((i * w, 0, w, h)))
        return images

    def get_by_id(self, id):
    #finds the specific sprite, then returns the sprites rect for clicking purposes
        for arrays in self.all_sprites:
            for sprites in arrays:
                if sprites.name == id and sprites.visible == True:
                    return sprites.rectangle
        print "Error, could not find sprite by index or sprite is currently set to visible."
        return pygame.draw.rect(everything.window_surface,(0, 0, 0), (0,0, 1, 1))

    def compile_images (self, tile_x, tile_y, str, fps,
        loop_start, start_frame, sprite_x, sprite_y, name):
        temp_sprite = self.load_sliced_sprites(tile_x, tile_y, str)
        sprites = []
        sprites.append(
            AnimatedSprite(
                temp_sprite, fps, loop_start, start_frame,
                sprite_x, sprite_y, name, tile_x, tile_y, loop_start))
        return sprites

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps, idle_tag,
        start_sprite, loc_x, loc_y, sprite_name, w, h, loop):
        self.stop = False
        self.x = loc_x
        self.y = loc_y
        self.name = sprite_name
        self.height = h
        self.width = w
        self.visible = True
        self.rectangle = pygame.draw.rect(
            everything.window_surface, 0, (self.x, self.y, w, h))
        self.idle = idle_tag
        pygame.sprite.Sprite.__init__(self)
        self._images = images
        self._start = pygame.time.get_ticks()
        self._delay = 3000 / fps
        self._last_update = 0
        self._frame = start_sprite
        self.my_start_sprite = 0
        self.update(pygame.time.get_ticks())
        self.h = h
        self.w = w

    def update(self, t):
        if (t - self._last_update) > self._delay:
            if self.idle == False: #when hovered over
                self._frame += 1
                if self._frame >= len(self._images) and self.stop == False:
                    self._frame = self.my_start_sprite
                elif self._frame >= len(self._images) and self.stop == True:
                    self._frame += -1
                
            if self.idle == True:
                self._frame = self.my_start_sprite # idle. 
                                # Could probably edit this slightly
                                # and make an idle animation
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
        self.update(pygame.time.get_ticks())
        if self.visible == True:
            everything.window_surface.blit(self.image, (self.x, self.y))
            
    def play(self):
        self.idle = False

    def play_once(self):
        #use to play the animation once
        self.idle = False
        self.stop = True
        
    def move(self, x, y):
        self.x += x
        self.y += y
        self.rectangle.move_ip(x,y)

class Background(object):
    def __init__(self,str):
        print 'Made background!' # Debug
        self.image = pygame.image.load(str) 
        everything.window_surface.blit(self.image, (0, 0))

    def update(self):
        everything.window_surface.blit(self.image, (0, 0))
        # What are the next two comments for? -- David (oddshocks)
        '''
        //image render
        '''
    def background_image(self,str):
        self.image = pygame.image.load(os.path.join('filtered/', str))

    '''
    //animations not 4 game
    '''

class MouseEventHandler(object):
    def __init__ (self, mouse_x, mouse_y):
        self.my_rect = pygame.draw.rect(
            everything.window_surface, 0, (mouse_x, mouse_y, 5, 5))
    def click(self, sprite_name):
        #print 'Mouse clicked!' 
        if self.my_rect.colliderect(graphics.get_by_id(sprite_name)):
            return True
    def update(self, mouse_x, mouse_y):
        self.my_rect = pygame.draw.rect(
            everything.window_surface, 0, (mouse_x, mouse_y, 5, 5))

class Game(object):
    def __init__(self):
        print 'Made game!' # Debug
        self.mouse_rect = None

    def update(self):
        '''
        if (
        '''

        # Can someone explain the below comments to me? -- odd
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

pygame.init() # Initialize pygame

everything = Everything()
game = Game()        
background = Background(str="kingarthur.png")
graphics = Graphics()
gui = GUI()
mouse = MouseEventHandler(0,0)
clock = pygame.time.Clock()

screenArray = []

# Big list of screens being built. Feel free to make it a function if you want

start = Screen("kingarthur.png")
start.addSprite("Dove")
start.isActive()
screenArray.append(start)

findSword = Screen ("screen1.png")
findSword.addSprite("ArthurStand")
findSword.addSprite("SwordWorld")
findSword.addSprite("GUIMapHitForest1")
findSword.addSprite("GUIMapHitForest2")
findSword.addSprite("GUIMapHitForest3")

screenArray.append(findSword)

Gawain_West = Screen ("Gawain.png")
Gawain_West.addSprite("ArthurStand")
Gawain_West.addSprite("DoveWorld")
Gawain_West.addSprite("RedKnightStand")
Gawain_West.addSprite("GreenKnight")
Gawain_West.addSprite("GUIMapHitGawain1")
Gawain_West.addSprite("GUIMapHitGawain2")

screenArray.append(Gawain_West)

Lancelot_Day = Screen ("LancelotDAY.png")
Lancelot_Day.addSprite("ArthurStand")
Lancelot_Day.addSprite ("BlueKnightWalk")
Lancelot_Day.addSprite ("WandWorld")
Lancelot_Day.addSprite ("GUIMapHitLancelot")

screenArray.append(Lancelot_Day)

Lancelot_Night = Screen ("LancelotNIGHT.png")
Lancelot_Night.addSprite("ArthurStand")
Lancelot_Night.addSprite("GrailWorld")
Lancelot_Night.addSprite("BlueKnightWalk")

screenArray.append(Lancelot_Night)

Merlin_Shack = Screen ("merlinshackOUTSIDE.png")
Merlin_Shack.addSprite("ArthurStand")
Merlin_Shack.addSprite ("Couldron")
Merlin_Shack.addSprite ("MerlinMagic")
Merlin_Shack.addSprite ("GUIMapHitShack")
screenArray.append(Merlin_Shack)

Castle_Halls = Screen ("castleHalls.png")
Castle_Halls.addSprite("ArthurStand")
Castle_Halls.addSprite ("GreenKnightWalk")
Castle_Halls.addSprite ("GUIMapHitCastleInside1")
Castle_Halls.addSprite ("GUIMapHitCastleInside2")
screenArray.append(Castle_Halls)

Castle = Screen ("outsideCasltleField.png")
Castle.addSprite("ArthurStand")
Castle.addSprite("GUIMapHitClearing1")
Castle.addSprite("GUIMapHitClearing2")
Castle.addSprite("GUIMapHitClearing3")
screenArray.append(Castle)

Keep = Screen ("keep.png")
Keep.addSprite("ArthurStand")
Keep.addSprite("MordredAttack")
Keep.addSprite("Monster")
Keep.addSprite("DoveSingWorld")
graphics.getSprite("DoveSingWorld").visible = False
Keep.addSprite("GUIMapHitKeep")
screenArray.append(Keep)

Agravain_Forest = Screen ("forestAgravain.png")
Agravain_Forest.addSprite("ArthurStand")
Agravain_Forest.addSprite("YellowKnightWalk")
Agravain_Forest.addSprite("GUIMapHitAgravain")
screenArray.append(Agravain_Forest)

Camelot = Screen ("banquethall.png")
screenArray.append(Camelot)

SwordClicked = False;
DoveClicked = False;
CouldronClicked = False;
WandClicked = False;
GrailClicked = False;
SwordClicked = False;
SDoveClicked = False;

### START THE GAME LOOP

quitting = False # Is the game closing?

while not quitting:
    clock.tick(30) # Set FPS to 30
    
    # Main event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'Got quit event' # DEBUG
            quitting = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print 'Got [esc] event' # DEBUG
                quitting = True
        if event.type == pygame.MOUSEMOTION:
            mouse.update(graphics.custom_mouse.x, graphics.custom_mouse.y)
            graphics.custom_mouse.x, graphics.custom_mouse.y = event.pos
            graphics.custom_mouse.old_x = graphics.custom_mouse.x
            graphics.custom_mouse.old_y = graphics.custom_mouse.y
            mouse_rect = pygame.draw.rect(
                everything.window_surface,
                (0, 0, 0), (graphics.custom_mouse.x,
                graphics.custom_mouse.y, 1, 1))
            if mouse_rect.y > 700:
                gui.rollover = True
            if mouse_rect.y < 700:
                gui.rollover = False
        if event.type == pygame.MOUSEBUTTONDOWN \
            and pygame.mouse.get_pressed():
            #Useful sprite control quick reference
            #graphics.getSprite("SPRITE_NAME").visible = False //sets sprite to be invisible (or visible is True). Useful for inventory items that are collected
            #graphics.getSprite("SPRITE_NAME").play_once() //plays the animation exactly once and stops at the last frame
            #graphics.getSprite("SPRITE_NAME").play() //plays, loops
            
                if start.active == True:
                    findSword.isActive()
                    #Title screen code. This moves to the first screen, so put inits for the logic for screen 1 after here
                    
                if  findSword.active == True:
                    #Logic for the first screen (arthur sword)
                    if mouse.click("GUIMapHitForest1"):
                        Gawain_West.isActive()
                    if mouse.click("GUIMapHitForest2"):
                        Lancelot_Day.isActive()
                    if mouse.click("GUIMapHitForest3"):
                        Merlin_Shack.isActive()
                    if mouse.click("SwordWorld"):
                        print ("Clicked on sword, collect it")
                        SwordClicked = True
                        graphics.getSprite("SwordWorld").visible = False
                        
                if Gawain_West.active == True:
                    # Logic for Gawain forest
                    if mouse.click("DoveWorld"):
                        print ("Collect dove")
                        DoveClicked = True
                        graphics.getSprite("DoveWorld").visible = False
                    if mouse.click("GUIMapHitGawain1"):
                        findSword.isActive()
                    if mouse.click("GUIMapHitGawain2"):
                        Castle_Halls.isActive()
                    #Give belt to Gawain: graphics.getSprite("GreenKnight").visible = False 

                if Merlin_Shack.active == True:
                    # Logic for Merlin's Shack
                    if mouse.click("GUIMapHitShack"):
                        findSword.isActive()
                    if mouse.click("Couldron"):
                        CouldronClicked = True
                        print ("Collect the soup + relevent text")
                    #Give wand to merlin: graphics.getSprite("MerlinMagic").play_once()
                        
                if Lancelot_Day.active == True:
                    # Logic for Lancelot (Day)
                    if mouse.click("WandWorld"):
                        print ("Add wand to inventory now and play text. Also make WandWorld invisible")
                        WandClicked = True
                        graphics.getSprite("WandWorld").visible = False
                    if mouse.click("GUIMapHitLancelot"):
                        findSword.isActive()
                    # if agravain and bors are helped: Lancelot_Night.active() (this should just skip the day one and jump to night... hopefully)
                        
                if Castle_Halls.active == True:
                    #Logic for Castle Hall (Bors room)
                    if mouse.click("GUIMapHitCastleInside1"):
                        Gawain_West.isActive()
                    if mouse.click("GUIMapHitCastleInside2"):
                        Castle.isActive()
                    #Giving Bors the soup does nothing other than set the trigger for Lancelot's quest.

                if Castle.active == True:
                    #No logic on this screen. This is purely a movement screen
                    if mouse.click("GUIMapHitClearing1"):
                        Castle_Halls.isActive()
                    if mouse.click("GUIMapHitClearing2"):
                        Agravain_Forest.isActive()
                    if mouse.click("GUIMapHitClearing3"):
                        Keep.isActive()

                if Keep.active == True:
                    # Logic for Mordred scene (Keep). When singing dove is used on Monster, monster and mordred(attack) play once. Also make dovesinging visible = true
                    if mouse.click("GUIMapHitKeep"):
                        Castle.isActive()

                if Agravain_Forest.active == True:
                    if mouse.click("DoveInventory"):
                        SDoveClicked = True
                        DoveClicked = False
                        
                    #Logic for Aggravain scene. Use dove on Agravain, the dove turns into the singing dove. Also a flag for Lancelot's quest (Must have helped Agravain and Bors)
                    if mouse.click("GUIMapHitAgravain"):
                        Castle.isActive()

                if Lancelot_Night.active == True:
                    if mouse.click("GrailWorld"):
                        GrailClicked = True
                        # play some text
                        Camelot.isActive()
                    #Logic for the last little interaction
                        
            #mouse.update(graphics.custom_mouse.x, graphics.custom_mouse.y)
            #current_screen += 1
            #screenArray[current_screen].isActive()

            #The following event shows how to make a "click to play once" event. This will play the animation exactly once, useful for the Monster event and Merlin's magic
            #if mouse.click("Dove"):
                #print 'Hit the dove!' # Debug
                #graphics.getSprite("Dove").play_once()
                
    # Update everything
    everything.update()

    # Update the screen
    pygame.display.flip()

### END THE GAME LOOP

pygame.quit() # Quit the game
