import random
import string

import pygame

from start import font, screen


def draw_lines(step: int, x: int, y: int):
    char = random.choice(string.ascii_letters)
    screen.blit(font.render(char, False, 'Green'), (x, y + step * 10))
    while step >= 0:
        surf = pygame.Surface((10, 10))
        surf.fill('Black')
        surf.set_alpha(50)
        screen.blit(surf, (x, y + step * 10))
        if y+step*10 > 1200:
            return 0
        step -= 1




async def end():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
# Узнать как это делается
