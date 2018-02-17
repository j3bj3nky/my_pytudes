# Advent of Code '16 Day 03: Squares With Three Sides
# JebJenky
# 2018-02-17


def countTris():

    """This function will simply count the amount of possible triangles from
       a file.all
    """

    possible = 0
    impossible = 0
    triFile = './triangles.txt'

    with open(triFile) as tf:
        sides = tf.readlines()
    sides = [x.strip() for x in sides]

    tf.close()

    for lists in sides:

        lists = lists.split(" ")

        for side in range(lists.count('')):
            lists.remove('')

        if (int(lists[0]) + int(lists[1])) > int(lists[2]) and \
           (int(lists[0]) + int(lists[2])) > int(lists[1]) and \
           (int(lists[2]) + int(lists[1])) > int(lists[0]):
            possible += 1
        else:
            impossible += 1

        del sides[0]

    print(possible)
    print(impossible)


countTris()
