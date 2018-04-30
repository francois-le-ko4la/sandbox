#!/usr/bin/env python

import curses 

screen = curses.initscr()

try:
    screen.border(0)

    for i in [1, 2, 3]:
        box1 = curses.newwin(4, 30, i * 5, 5)
        box1.box()    
        screen.refresh()
        box1.refresh()

    screen.getch()

finally:
    curses.endwin()
