import hashlib

puzzle_input = 'wtnhxymk'
num = 0
i = 0
code = ''


while len(code) < 8:
    while len(code) == num:
        md5 = hashlib.md5((bytes(puzzle_input + str(i), encoding='utf-8'))).hexdigest()
        if md5[0:5] == '00000':
            code += md5[5]
        else:
            i += 1
    i += 1
    num += 1


print(code)
