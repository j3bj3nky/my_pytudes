import re


text = "triangles.txt"

text = open(text)


def is_triangle(sides):
    x, y, z = sorted(sides)
    return z < x + y


def parse_ints(text):
    return [int(x) for x in re.findall(r'\d+', text)]


triangles = [parse_ints(line) for line in text]

sum(map(is_triangle, triangles))


def invert(triangles):
    for i in range(0, len(triangles), 3):
        yield from zip(*triangles[i:i+3])


print(sum(map(is_triangle, invert(triangles))))
