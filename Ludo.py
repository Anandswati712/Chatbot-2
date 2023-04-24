import sys
import pygame
import random

def dice():
    print(random.randint(1,6))

# dice()

width = 750
height = 750
white = (255,255,255)
red = (255,0,0)
blue = (0,0,204)
green = (0,153,76)
yellow = (255,255,0)
black = (0,0,0)

game_display = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

def main():
    global game_display, clock
    game_display.fill(black)
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()      
        pygame.display.update()

def drawGrid():
    blockSize = 50
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(game_display, white,rect,1)

class ludo:
    def __init__(self,color):
        self.x = random.randrange(0,width)
        self.y = random.randrange(0,height)
        self.size  = random.randrange(8,8)
        self.color = color
        pygame.init()

   

# def main():

if __name__ == '__main__':
    main()