'''
Main file for arthur-point-and-click
'''

import pygame, sys

def main():

	### CONSTANTS ###
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	RED = 255, 0, 0

	### INITIALIZE ###
	pygame.init()

	### WINDOW FRAME ###
	screen = pygame.display.set_mode((640, 480)) # resolution tentative
	pygame.display.set_caption("arthur-point-and-click")

	### GAME LOOP ###
	clock = pygame.time.Clock() # framerate control for animation
	while True:
		clock.tick(50)

		# Event processing
		for event in pygame.event.get():
			# Quitting?
			if event.type == pygame.QUIT:
				sys.exit()

		# Get a black background
		screen.fill(BLACK)

		# Add some title-ish text, just to do something
		title_font = pygame.font.SysFont("sans-serif", 48)
		title_surface = title_font.render("Arthur", True, RED)
		screen.blit(title_surface, (100, 100))

		# Update the screen
		pygame.display.flip()


# Start the game
main() # this may be done a different way in the future
