#!/usr/bin/python3

import pygame
from checkersgame2.constants import WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')

def main():
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

if __name__ == "__main__":
    main()
