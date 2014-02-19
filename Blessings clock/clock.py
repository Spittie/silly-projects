from blessings import Terminal
import arrow
import time
import sys


def print_array(array, x, y):
    for l in array:
        for c in l:
            with t.location(x, y):
                sys.stdout.write(c)
        y += 1
        print

t = Terminal()

zer = [['#####'],
       ['#   #'],
       ['#   #'],
       ['#   #'],
       ['#####']]

uno = [['  #  '],
       [' ##  '],
       ['# #  '],
       ['  #  '],
       [' ### ']]

due = [['#### '],
       ['    #'],
       [' ### '],
       ['#    '],
       [' ####']]

tre = [['#####'],
       ['    #'],
       [' ### '],
       ['    #'],
       ['#####']]

qua = [['#    '],
       ['#    '],
       ['# #  '],
       ['#####'],
       ['  #  ']]

cin = [['#####'],
       ['#    '],
       ['#### '],
       ['    #'],
       ['#### ']]

sei = [['#####'],
       ['#    '],
       ['#####'],
       ['#   #'],
       ['#####']]

set = [['#####'],
       ['    #'],
       ['   # '],
       ['  #  '],
       ['  #  ']]

ott = [['#####'],
       ['#   #'],
       ['#####'],
       ['#   #'],
       ['#####']]

nov = [['#####'],
       ['#   #'],
       ['#####'],
       ['    #'],
       ['#####']]

sep = [['     '],
       ['  #  '],
       ['     '],
       ['  #  '],
       ['     ']]


while 1:
    with t.fullscreen():
        print t.clear()
        y = 0
        x = 0
        for i in arrow.now().format('H:mm:ss'):
            if i == str(0):
                print_array(zer, x, y)
            if i == str(1):
                print_array(uno, x, y)
            if i == str(2):
                print_array(due, x, y)
            if i == str(3):
                print_array(tre, x, y)
            if i == str(4):
                print_array(qua, x, y)
            if i == str(5):
                print_array(cin, x, y)
            if i == str(6):
                print_array(sei, x, y)
            if i == str(7):
                print_array(set, x, y)
            if i == str(8):
                print_array(ott, x, y)
            if i == str(9):
                print_array(nov, x, y)
            if i == ':':
                print_array(sep, x, y)
            x += 6
        time.sleep(1)

