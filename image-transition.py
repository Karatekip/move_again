# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:15:39 2024

@author: camil.caudron
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fade Transition")

# Load two images (ensure they have the same dimensions as the screen)
image1 = pygame.image.load('graphics/balloon_view.jpg').convert()
image2 = pygame.image.load('graphics/ski_view.jpg').convert()

# Scale the images to fit the screen
image1 = pygame.transform.scale(image1, (screen_width, screen_height))
image2 = pygame.transform.scale(image2, (screen_width, screen_height))

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Fade transition function
def fade_transition(image1, image2, duration):
    # Loop through alpha values from 0 to 255 for fading
    for alpha in range(0, 256):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the first image (the background)
        screen.blit(image1, (0, 0))

        # Set the alpha (transparency) for the second image
        image2.set_alpha(alpha)

        # Draw the second image on top of the first
        screen.blit(image2, (0, 0))

        # Update the display
        pygame.display.update()

        # Control the speed of the fade
        clock.tick(duration)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Call the fade transition function
    fade_transition(image1, image2, 60)  # 60 is the duration controlling the speed of the transition

    # Once fade is done, wait for a moment and exit
    pygame.time.wait(2000)  # Wait for 2 seconds
    running = False

# Quit Pygame
pygame.quit()
