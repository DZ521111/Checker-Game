'''
Author : Dhruv B Kakadiya

'''

import pygame as pg
from modules import statics as st

# static variables for this perticular file
fps = 60

WIN = pg.display.set_mode((st.width, st.height))
pg.display.set_caption("Checkers")

# main function
if __name__ == '__main__':

    # represents the game
    run = True

    # certain clock value default because it is varries from diff pc to pc
    clock = pg.time.Clock()

    # main loop
    while (run):
        clock.tick(fps)

        # check if any events is running or not
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                run = False
    pg.quit()