import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.direction = 'right'
        self.body = pygame.image.load(".\\source\\block_snake.jpg")

    def change_direction(self, new_direction):
        self.direction = new_direction
    
    def move_snake(self):
        if self.direction == 'right':
            self.x += 10
        elif self.direction == 'left':
            self.x -= 10
        elif self.direction == 'up':
            self.y -= 10
        elif self.direction == 'down':
            self.y += 10

    def draw_snake(self):
        self.move_snake()
        display.fill((0, 0, 0))
        display.blit(self.body, (snake.x,snake.y))
        pygame.display.flip()
    

if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode((500,500))

    snake = Snake()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    #user clicked the right arrow
                    snake.change_direction('right')
                elif event.key == K_LEFT:
                    #user clicked the left arrow
                    snake.change_direction('left')
                elif event.key == K_UP:
                    #user clicked the up arrow
                    snake.change_direction('up')
                elif event.key == K_DOWN:
                    #user clicked the down arrow
                    snake.change_direction('down')
            elif event.type == QUIT:
                running = False
        snake.draw_snake()
        time.sleep(0.3)