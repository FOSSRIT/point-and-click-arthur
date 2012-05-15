import os
import pygame
import random
import sys
from pygame.locals import *
from random import randint

### CONSTANTS
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
TEXT_COLOR = (255, 255, 255)

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
        game.update()       
        gui.update()
        background.update()
        graphics.update()

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
                "King Arthur: \"Welcome to my Game!\"", everything.font,\
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
        for arrays in self.all_sprites:
            for sprites in arrays:
                sprites.location = (sprites.x, sprites.y, 100)
                if sprites.name == "Walking":
                    sprites.x += 3                    
                sprites.render(everything.window_surface)
        self.custom_mouse.update()

    def load_all_sprites(self):
        self.all_sprites.append(self.compile_images(
            72, 104, 'walktest.png', 20, False, 0, 200, 100, "Walking"))
        self.all_sprites.append(self.compile_images(
            48, 48, 'birdsprite.png', 20, True, 1, 300, 100, "Dove"))

    def load_sliced_sprites(self, w, h, file_name):
        images = []
        master_image = pygame.image.load(
            os.path.join('', file_name)).convert_alpha()
        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width / w)):
            images.append(master_image.subsurface((i * w, 0, w, h)))
        return images

    def compile_images (self, tile_x, tile_y, str, fps,
        loop_start, start_frame, sprite_x, sprite_y, name):
        temp_sprite = self.load_sliced_sprites(tile_x, tile_y, str)
        sprites = []
        sprites.append(
            AnimatedSprite(
                temp_sprite, fps, loop_start, start_frame,\
                sprite_x, sprite_y, name, tile_x, tile_y))
        return sprites

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps, idle_tag,\
        start_sprite, loc_x, loc_y, sprite_name, w, h):
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
        self.my_start_sprite = start_sprite 
        self.update(pygame.time.get_ticks())

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
            self.rectangle.move(self.x, self.y)
            everything.window_surface.blit(self.image, (self.x, self.y))

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
        pygame.image.load(str)

    '''
    //animations not 4 game
    '''

class MouseEventHandler(pygame.Rect):
    def __init__(self, mouse_x, mouse_y):
        self.my_rect = pygame.draw.rect(
            everything.window_surface, 0, (mouse_x, mouse_y, 5, 5))
    def click(self, temp_rect):
        print 'Mouse clicked!' # Debug
        if self.my_rect.colliderect(temp_rect):
            return True

class Game(object):
    def __init__(self):
        print 'Made game!' # Debug
        self.mouse_rect = None

    def update(self):
                                

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

clock = pygame.time.Clock()

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
            mouse_rect = MouseEventHandler(
                graphics.custom_mouse.x, graphics.custom_mouse.y)
            for arrays in graphics.all_sprites:
                for sprite in arrays:
                    if (sprite.name == "Dove"):
                        if mouse_rect.click(sprite.rectangle):
                            print 'Hit the dove!' # Debug
                            gui.display_text = True
    # Update everything
    everything.update()

    # Update the screen
    pygame.display.flip()

### END THE GAME LOOP

pygame.quit() # Quit the game
