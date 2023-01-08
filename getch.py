#!/usr/bin/python
# -*- coding: utf-8 -*-

# Take _Getch from bm.py after understanding it that was given in link provided by you(TA)
# So that i can use getchar function to take input
import gameConfig


class _Getch:

    """Gets a single character from standard input. Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

    def Set_Frame_rate(self, frame_rate):
        self.impl.fps = frame_rate


class _GetchUnix:

    def __init__(self):
        import tty
        import sys
        from select import select
        self.fps = 1

    def __call__(self):
        import sys
        import tty
        import termios
        from select import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            [i, o, e] = select([sys.stdin.fileno()], [], [],
                               abs((7 - self.fps)) / 5.8)
            if i:
                ch = sys.stdin.read(1)
            else:
                ch = None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
