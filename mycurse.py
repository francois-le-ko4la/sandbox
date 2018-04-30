import curses
from math import *


class CursesStatusBar(object):
    def __init__(self, screen, text, color):
        height, width = screen.getmaxyx()
        screen.attron(color)
        screen.addstr(height-1, 0, text)
        screen.addstr(height-1, len(text), " " * (width - len(text) - 1))
        screen.attroff(color)



class MyCurses(object):
    def __init__(self):

        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.screen.keypad( 1 )
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def build(self):
        highlightText = curses.color_pair( 2 )
        normalText = curses.A_NORMAL
        self.screen.border( 0 )
        curses.curs_set( 0 )
        columns = 5
        string = "Lorem ipsum dolor sit amet consectetuer metus nec eu C urabitur eleifen."
        self.screen.addstr(1,1,string)
        self.screen.addstr(20,1,"Press ESC to EXIT")

        myStatus = CursesStatusBar(self.screen, "Mon texte", curses.color_pair(3))


        self.screen.refresh()
        rows = int(ceil(len(string)/columns))
        box = curses.newwin(rows + 2, columns + 2, 3, 1)
        box.box()
        for row in range(1,rows+1):
            box.addstr(row,1,string[(row*columns)-columns:(row*columns)])
            box.refresh()

        x = self.screen.getch()
        while x != 27:
            x = self.screen.getch()
        curses.endwin()

myscreen = MyCurses()
myscreen.build()

