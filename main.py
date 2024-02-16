import random

import pygame

from func import draw_lines
from start import clock


class Line:
    step = 0

    def __init__(self):
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 800)


lines = []

running = True
while running:

    for line in lines:
        if draw_lines(line.step, line.x, line.y) == 0:
            lines.remove(line)
        else:
            line.step += 1

    a = Line()
    lines.append(a)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(60)
