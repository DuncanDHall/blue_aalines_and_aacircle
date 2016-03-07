import pygame
from pygame.locals import *
from pygame import gfxdraw


pygame.init()

screen = pygame.display.set_mode((300, 300))

while True:
    screen.fill(pygame.Color(200, 200, 200))

    # screen.fill((0, 0, 0))

    # Filling with black makes the following work...
    # It therefore seems that somehow aacircle is getting it's blue
    #  value from max(background_blue_channel, specified_blue_channel)
    # The left circle is still blue when drawn on black. This is only
    # for aa circle though, aalines seems to just override specified 
    # channel value with background blue channel value...

    gfxdraw.aacircle(
        screen,
        50,
        150,
        30,
        (0, 0, 255)
    )

    gfxdraw.aacircle(
        screen,
        130,
        150,
        30,
        (255, 0, 0)
    )

    pygame.draw.aalines(
        screen,
        (0, 0, 255, 0),
        True,
        [(20, 20), (250, 50), (200, 10)],
        1
    )

    # We're also having issues with alpha values (it's not as simple as adding
    #  a fourth parameter to the color), but we haven't done that much looking
    #  yet

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
