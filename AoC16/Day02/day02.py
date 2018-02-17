# Advent of Code '16 Day 02: Bathroom Security
# JebJenky
# 2018-02-17


def checkOver(a, b):

    """This function will check whether the x and y values have gone past the
    limit of the keypad.
    """
    global x
    global y
    a = x
    b = y

    if (a > 3) or (b > 3):
        if (a > 3):
            a = 3
        else:
            b = 3
    elif (a < 1) or (b < 1):
        if (a < 1):
            a = 1
        else:
            b = 1

    x = a
    y = b


# import lists from files and clean them up
aocInput = './aocInput.txt'
with open(aocInput) as f:
    list1 = f.readline()
    list2 = f.readline()
    list3 = f.readline()
    list4 = f.readline()
    list5 = f.readline()

list1 = [x.strip() for x in list1]
list2 = [x.strip() for x in list2]
list3 = [x.strip() for x in list3]
list4 = [x.strip() for x in list4]
list5 = [x.strip() for x in list5]

if list1[-1] == '':
    del list1[-1]
if list2[-1] == '':
    del list2[-1]
if list3[-1] == '':
    del list3[-1]
if list4[-1] == '':
    del list4[-1]
if list5[-1] == '':
    del list5[-1]

f.close()

# make a list of lists called directions
directions = [list1, list2, list3, list4, list5]

# initialize the number array
nums = []


def codeLoop():

    """ This is the main block of code that will loop over the directions
        and check them for the numbers of the keypad.
    """
    global x
    global y
    num = 0

    for list in directions:
        for move in list:

            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

            checkOver(x, y)

        if x == 1 and y == 3:
            num = 1
        elif x == 2 and y == 3:
            num = 2
        elif x == 3 and y == 3:
            num = 3
        elif x == 1 and y == 2:
            num = 4
        elif x == 2 and y == 2:
            num = 5
        elif x == 3 and y == 2:
            num = 6
        elif x == 1 and y == 1:
            num = 7
        elif x == 2 and y == 1:
            num = 8
        elif x == 3 and y == 1:
            num = 9

        nums.append(num)

    # show the list of nums
    print(nums)


# call to above function, codeLoop()
x = 2
y = 2
codeLoop()
