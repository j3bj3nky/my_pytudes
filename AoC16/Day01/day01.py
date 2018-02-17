# Jeb Jenkins(jeb_jenky)
# 2018-02-16
# Day01 Advent of Code 2016 solution


def taxiDist():

    """This function will take an array of directions in the format of
       R## or L##.  These will be used to compute the p and q for the
       Taxicab Distance sum. This equation is: d1(p,q) = sum(abs(Pi - Qi))
       We will see how it goes...abs
    """

    # the first thing to do is populate the directions array
    directions = ['L2', 'L5', 'L5', 'R5', 'L2', 'L4', 'R1', 'R1', 'L4', 'R2',
                  'R1', 'L1', 'L4', 'R1', 'L4', 'L4', 'R5', 'R3', 'R1', 'L1',
                  'R1', 'L5', 'L1', 'R5', 'L4', 'R2', 'L5', 'L3', 'L3', 'R3',
                  'L3', 'R4', 'R4', 'L2', 'L5', 'R1', 'R2', 'L2', 'L1', 'R3',
                  'R4', 'L193', 'R3', 'L5', 'R45', 'L1', 'R4', 'R79', 'L5',
                  'L5', 'R5', 'R1', 'L4', 'R3', 'R3', 'L4', 'R185', 'L5', 'L3',
                  'L1', 'R5', 'L2', 'R1', 'R3', 'R2', 'L3', 'L4', 'L2', 'R2',
                  'L3', 'L2', 'L2', 'L3', 'L5', 'R3', 'R4', 'L5', 'R1', 'R2',
                  'L2', 'R4', 'R3', 'L4', 'L3', 'L1', 'R3', 'R2', 'R1', 'R1',
                  'L3', 'R4', 'L5', 'R2', 'R1', 'R3', 'L3', 'L2', 'L2', 'R2',
                  'R1', 'R2', 'R3', 'L3', 'L3', 'R4', 'L4', 'R4', 'R4', 'R4',
                  'L3', 'L1', 'L2', 'R5', 'R2', 'R2', 'R2', 'L4', 'L3', 'L4',
                  'R4', 'L5', 'L4', 'R2', 'L4', 'L4', 'R4', 'R1', 'R5', 'L2',
                  'L4', 'L5', 'L3', 'L2', 'L4', 'L4', 'R3', 'L3', 'L4', 'R1',
                  'L2', 'R3', 'L2', 'R1', 'R2', 'R5', 'L4', 'L2', 'L1', 'L3',
                  'R2', 'R3', 'L2', 'L1', 'L5', 'L2', 'L1', 'R4']

    # initialize curX and curY
    curX = 0
    curY = 0
    p1 = 0
    q1 = 0

    # startDir initialization
    startDir = 'N'

    # loop for directions
    for direction in directions:

        # need turn and steps
        turn = direction[0]
        steps = int(direction[1:])

        # if...else for startDir & curDir

        if startDir == 'N':
            if turn == 'L':
                curDir = 'W'
            elif turn == 'R':
                curDir = 'E'

        elif startDir == 'W':
            if turn == 'L':
                curDir = 'S'
            elif turn == 'R':
                curDir = 'N'

        elif startDir == 'S':
            if turn == 'L':
                curDir = 'E'
            elif turn == 'R':
                curDir = 'W'

        elif startDir == 'E':
            if turn == 'L':
                curDir = 'N'
            elif turn == 'R':
                curDir = 'S'

        # if ... else for curX and curY

        if curDir == 'W':
            curX -= steps
        elif curDir == 'N':
            curY += steps
        elif curDir == 'S':
            curY -= steps
        elif curDir == 'E':
            curX += steps

        # set new startDir
        startDir = curDir

    sumD = abs(p1 - q1) + abs(curX - curY)
    print(sumD)


taxiDist()
