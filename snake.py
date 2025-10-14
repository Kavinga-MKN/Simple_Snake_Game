import pygame, sys
from pygame.math import Vector2

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cels = 25

class Food:
    def __init__(self):
        self.position = Vector2(5,6)

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)

screen = pygame.display.set_mode((cell_size*number_of_cels, cell_size*number_of_cels))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()

food = Food()
food_surface = pygame.image.load("Graphics/food.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    screen.fill(GREEN)
    food.draw()
    pygame.display.update()
    clock.tick(60)