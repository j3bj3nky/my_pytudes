import hashlib

puzzle_input = 'wtnhxymk'
i = 0
code = [None] * 8


while None in code:
    md5 = hashlib.md5((bytes(puzzle_input + str(i), encoding='utf-8'))).hexdigest()
    if md5[0:5] == '00000':
        position = int(md5[5], 16)
        if position < 8 and code[position] is None:
            code[position] = md5[6]

    i += 1


print(code)
