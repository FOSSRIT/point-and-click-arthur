'''
Main file for arthur-point-and-click
'''

import pygame, sys

def main():

	### INITIALIZE ###
    pygame.init()

	### WINDOW FRAME ###
	screen = pygame.display.set_mode(640, 480) # resolution tentative
	pygame.display.set_caption("arthur-point-and-click")

	### GAME LOOP ###
	clock = pygame.time.Clock() # framerate control for animation
	while True
		clock.tick(50)

		# Event processing
		for event in pygame.event.get():
			# Quitting?
			if event.type == pygame.QUIT:
				sys.exit()

		# Update the screen
		pygame.display.flip()
