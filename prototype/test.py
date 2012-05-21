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
'''

class Everything(object):
    def __init__(self):
        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH,
            WINDOW_HEIGHT))
        self.font = pygame.font
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 48)
        pygame.display.set_caption('Point And Prototype')
        pygame.mouse.set_visible(False)

    def draw_text(self, text, font, surface, x, y):
        text_obj = font.render(text, 1, TEXT_COLOR)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def update(self):
        self.window_surface.fill((0,0,0))
        game.update()       
        gui.update()
        background.update()
        for screens in screenArray:
            screens.update()
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
        print "Loading " + sprite
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
        save_box = pygame.draw.rect(
            everything.window_surface, (255, 255, 0), (1100, 0, 100, 50))
        save_text = everything.draw_text(
            "Save", everything.font,everything.window_surface, 1110, 10)
        # Current issue: Rect doesnt show up,
        # but this becomes irrelevant when the GUI becomes sprite based
        # oddshocks: it is possible that I fixed this, not sure
        self.inventory = pygame.draw.rect(
            everything.window_surface, (255, 255, 0), (300, 1000, 700, 180))
        print 'Made GUI!' # Debug

    def update(self):
        if self.rollover == True:
            everything.draw_text(
                "Inventory", everything.font,
                everything.window_surface, 300, 780) 
            self.inventory = self.inventory.move(300, 820)
        elif self.rollover == False:
            self.inventory = self.inventory.move(300, 1000)
        if self.display_text == True:
            text_box = pygame.draw.rect(
                everything.window_surface, (255, 255, 0), (300, 0, 700, 100))
            everything.draw_text(
                "King Arthur: \"Welcome to my Game!\"", everything.font,
                everything.window_surface, 310, 10) 
        elif self.display_text == False:
            text_box = pygame.draw.rect(
                everything.window_surface, (255, 255, 0), (300, 0, 0, 0))

class Graphics(object):
    def __init__(self):
        self.custom_mouse = MyMouse()
        self.all_sprites = []
        self.load_all_sprites()
    def update(self):
        self.custom_mouse.update()

    def load_all_sprites(self):
        self.all_sprites.append(self.compile_images(
            48, 48, 'birdsprite.png', 20, True, 1, 250, 315, "Dove"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALK.png', 20, True, 0, 200, 100, "RedKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKGREEN.png', 20, True, 0, 200, 100, "GreenKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKBLUE.png', 20, True, 0, 200, 100, "BlueKnightWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKMORDRED.png', 20, True, 0, 200, 100, "MordredWalk"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'knightWALKYELLOW.png', 20, True, 0, 200, 100, "YellowKnightWalk"))
        self.all_sprites.append(self.compile_images(
            53, 97, 'arthurstand.png', 20, False, 0, 150, 550, "ArthurStand"))
        self.all_sprites.append(self.compile_images(
            124, 128, 'merlinMagic.png', 20, True, 1, 450, 400, "MerlinMagic"))
        self.all_sprites.append(self.compile_images(
            64, 96, 'arthurWALK.png', 20, True, 0, 500, 500, "ArthurWalk"))
        self.all_sprites.append(self.compile_images(
            76, 72, 'couldron.png', 20, False, 1, 610, 325, "Couldron"))
        self.all_sprites.append(self.compile_images(
            60, 100, 'greenknight.png', 20, False, 1, 400, 550, "GreenKnight"))
        self.all_sprites.append(self.compile_images(
            700, 180, 'GUIInventory.png', 20, False, 1, 500, 500, "GUIInventory"))
        self.all_sprites.append(self.compile_images(
            90, 90, 'GUIMaphit.png', 20, False, 1, 500, 500, "GUIMapHit"))
        self.all_sprites.append(self.compile_images(
            100, 50, 'GUISave.png', 20, False, 1, 500, 500, "GUISave"))
        self.all_sprites.append(self.compile_images(
            126, 120, 'itemsINVENTORY.png', 20, False, 1, 500, 500, "InventoryItems"))
        self.all_sprites.append(self.compile_images(
            120, 100, 'itemsWORLD.png', 20, False, 1, 500, 500, "InventoryWorld"))
        self.all_sprites.append(self.compile_images(
            100, 132, 'knight-attackMORDRED.png', 20, False, 1, 500, 500, "MordredAttack"))
        self.all_sprites.append(self.compile_images(
            60, 96, 'knightstand.png', 20, False, 1, 500, 500, "RedKnightStand"))
        self.all_sprites.append(self.compile_images(
            76, 120, 'merlinWALK.png', 20, False, 1, 500, 500, "MerlinWalk"))
       
    def getSprite(self, sprite):
        print "Looking for " + sprite
        for arrays in self.all_sprites:
            for sprites in arrays:
                print "Sprites: Looking at " + sprites.name + " Comparing it to " + sprite
                if sprites.name == sprite:
                    print "Found sprite!"
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
                if sprites.name == id:
                    return sprites.rectangle
        print "Error, could not find sprite by index"
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
        self.my_start_sprite = loop
        self.update(pygame.time.get_ticks())
        self.h = h
        self.w = w

    def update(self, t):
        if (t - self._last_update) > self._delay:
            if self.idle == False: #when hovered over
                self._frame += 1
                if self._frame >= len(self._images):
                    self._frame = self.my_start_sprite
                
            if self.idle == True:
                self._frame = 0 # idle. 
                                # Could probably edit this slightly
                                # and make an idle animation
            self.image = self._images[self._frame]
            self._last_update = t
            
    def render(self, screen):
        self.update(pygame.time.get_ticks())
        if self.visible == True:
            everything.window_surface.blit(self.image, (self.x, self.y))

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
        print 'Mouse clicked!' # Debug
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

start = Screen("kingarthur.png")

start.addSprite("Dove")
start.isActive()
screenArray.append(start)

findSword = Screen ("screen1.png")
findSword.addSprite("ArthurStand")
#Add sword from GUI 
screenArray.append(findSword)

Gawain_West = Screen ("Gawain.png")
Gawain_West.addSprite("ArthurStand")
Gawain_West.addSprite("RedKnightStand")
Gawain_West.addSprite("GreenKnight")
#Add dove from GUI
screenArray.append(Gawain_West)

Lancelot_Day = Screen ("LancelotDAY.png")
Lancelot_Day.addSprite("ArthurStand")
Lancelot_Day.addSprite ("BlueKnightWalk")
#Add wand from GUI
screenArray.append(Lancelot_Day)

Lancelot_Night = Screen ("LancelotNIGHT.png")
Lancelot_Night.addSprite("ArthurStand")
Lancelot_Night.addSprite("BlueKnightWalk")
#Add grail from GUI
screenArray.append(Lancelot_Night)

Merlin_Shack = Screen ("merlinshackOUTSIDE.png")
Merlin_Shack.addSprite("ArthurStand")
Merlin_Shack.addSprite ("Couldron")
Merlin_Shack.addSprite ("MerlinMagic")
screenArray.append(Merlin_Shack)

Castle_Halls = Screen ("castleHalls.png")
Castle_Halls.addSprite("ArthurStand")
Castle_Halls.addSprite ("GreenKnightWalk")
screenArray.append(Castle_Halls)

Castle = Screen ("outsideCasltleField.png")
Castle.addSprite("ArthurStand")
screenArray.append(Castle)

Keep = Screen ("keep.png")
Keep.addSprite("ArthurStand")
screenArray.append(Keep)

Agravain_Forest = Screen ("forestAgravain.png")
Agravain_Forest.addSprite("ArthurStand")
screenArray.append(Agravain_Forest)

Camelot = Screen ("banquethall.png")
screenArray.append(Camelot)

current_screen = 0

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
            mouse.update(graphics.custom_mouse.x, graphics.custom_mouse.y)
            current_screen += 1
            screenArray[current_screen].isActive()
            '''if mouse.click("Dove"):
                print 'Hit the dove!' # Debug
                gui.display_text = True
                findSword.isActive()
                
            if mouse.click("RedKnightWalk"):
                print 'Hit the Red Knight!' # Debug
                gui.display_text = True'''
    # Update everything
    everything.update()

    # Update the screen
    pygame.display.flip()

### END THE GAME LOOP

pygame.quit() # Quit the game
