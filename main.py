#!/usr/bin/env python3

import sys,os
import curses

colors = {
    "BLUE/YELLOW" : 1,
    "BLACK/YELLOW": 2,
    "WHITE/YELLOW": 3,
}

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        # Render borders
        for i in range(0, 9 * 3 + 1 * 10):
            stdscr.addch(0, i, curses.ACS_HLINE, curses.color_pair(colors["BLACK/YELLOW"]))
        for i in range(0, 9 * 3 + 1 * 10):
            stdscr.addch(4, i, curses.ACS_HLINE, curses.color_pair(colors["WHITE/YELLOW"]))

        # Render status bar
        # stdscr.attron(curses.color_pair(3))
        # stdscr.addstr(height-1, 0, statusbarstr)
        # stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        # stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        # stdscr.attron(curses.color_pair(2))
        # stdscr.attron(curses.A_BOLD)

        # Rendering title
        # stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        # stdscr.attroff(curses.color_pair(2))
        # stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        # stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        # stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        # stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        # stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()