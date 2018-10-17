#!/usr/bin/python36

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
#pygame.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.music.play()
pygame.event.wait()

