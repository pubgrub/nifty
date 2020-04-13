print( "Hello World")

board = [   0, 7, 
            0, 8, 
            0, 8, 
            0, 11, 
            0, 11,
            0, 14,
            0, 15,
            0, 15,
            0, 15,
            2, 14,
            5, 11,
            5, 14,
            5, 14,
            6, 13,
            7, 12,
            7, 12,
            9, 10,
            9, 10,
            10, 9  ]

# Sticks:   0 rot
#           1 schwarz
#           2 hellbraun
#           3 dunkelbraun

stick = [   [ 4, 1, 2, 3, 1, 3, 2, 1, 3, 2, 3, 2, 2], [], [], [],
            [ 4, 2, 3, 3, 1, 2, 4, 2, 1, 3, 3], [], [], [],
            [ 5, 3, 3, 4, 2, 1, 2, 3, 5], [], [], [],
            [ 4, 4, 3, 2, 2, 1, 2, 1, 1, 3, 2, 1, 2], [], [], []
        ]

print( len(stick))

def drawStick( s):
    return

def stickToGrid( s, l):
    # s: List von Längen, immer rechts, runter, rechts, runter...
    # l: Breite des Grids
    g = []
    d = 0 # direction, 0 = rechts, 1 = runter
    for i in s:
        if d == 0:
            g.extend( [1] * i)
        else:
            for j in range(i):
                g.extend( [0] * (l - 1))
                g.append( 1)
        d = 1 - d
    return g

def printGrid( g, l):
    n = 0
    for i in g:
        print( i, end='')
        n +=1
        if n == l:
            n = 0
            print()
    print()

g = stickToGrid( stick[0], 19)
printGrid( g, 19)


g = []
g.append( 0)
g.extend( [1] * 5)
print( '----')
for i in g:
    print( i)