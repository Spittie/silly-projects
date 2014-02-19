from blessings import Terminal
import numpy
import time
import sys

t = Terminal()
with t.fullscreen():
    #h = t.height
    #w = t.width

    w = 40
    h = 40

    board = numpy.zeros((w, h))
    changes = numpy.zeros((w, h))
    numpy.set_printoptions(threshold=numpy.nan)

    # Block
    # board[30][30] = 1
    # board[30][31] = 1
    # board[31][31] = 1
    # board[31][30] = 1

    # Glider
    # board[2][4] = 1
    # board[3][2] = 1
    # board[4][3] = 1
    # board[3][4] = 1
    # board[4][4] = 1

    # Glider gun
    board[6][2] = 1
    board[7][2] = 1
    board[6][3] = 1
    board[7][3] = 1
    board[4][14] = 1
    board[4][15] = 1
    board[5][13] = 1
    board[6][12] = 1
    board[7][12] = 1
    board[8][12] = 1
    board[9][13] = 1
    board[10][14] = 1
    board[10][15] = 1
    board[7][16] = 1
    board[5][17] = 1
    board[9][17] = 1
    board[6][18] = 1
    board[7][18] = 1
    board[8][18] = 1
    board[7][19] = 1
    board[6][22] = 1
    board[5][22] = 1
    board[4][22] = 1
    board[6][23] = 1
    board[5][23] = 1
    board[4][23] = 1
    board[3][24] = 1
    board[7][24] = 1
    board[2][26] = 1
    board[3][26] = 1
    board[7][26] = 1
    board[8][26] = 1
    board[4][36] = 1
    board[5][36] = 1
    board[4][37] = 1
    board[5][37] = 1

    iterations = 0

    while 1:
        time.sleep(0.1)
        iterations += 1
        with t.location(0, 0):
            #print numpy.array_str(board, max_line_width=100000)
            for x in range(w):
                for y in range(h):
                    if board[x][y] == 1:
                        sys.stdout.write("@")
                    else:
                        sys.stdout.write(" ")
                print
            print 'Tick: ' + str(iterations)

            for x in range(w):
                for y in range(h):
                    neighbours = 0

                    try:
                        for nx in [-1, 0, 1]:
                            for ny in [-1, 0, 1]:
                                if not (nx == 0 and ny == 0):
                                    if board[x + nx][y + ny] == 1:
                                        neighbours += 1
                    except IndexError:
                        pass

                    changes[x][y] = board[x][y]
                    if board[x][y] == 1:
                        if neighbours < 2:
                            changes[x][y] = 0
                        if neighbours > 3:
                            changes[x][y] = 0
                    if board[x][y] == 0:
                        if neighbours == 3:
                            changes[x][y] = 1
            board = changes
            changes = numpy.zeros((w, h))