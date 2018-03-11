import numpy as np
import re

regex = re.compile(r'\d+')
a = np.zeros(shape=(6, 50))

f = open("input08.txt")
inp = f.readline()

while inp:
    line = inp.rstrip()

    nums = regex.findall(line)
    A = nums[0]
    B = nums[1]
    A = int(A)
    B = int(B)

    if "rect" in line:
        a[0:B, 0:A] = 1
    elif "rotate row" in line:
        a[A] = np.roll(a[A], B, axis=0)
    elif "rotate column" in line:
        a[:, A] = np.roll(a[:, A], B, axis=0)

    inp = f.readline()

f.close()

print((a == 1).sum())

letters = np.split(a, 10, axis=1)
for i in range(10):
    print(letters[i])
    print("\n")
