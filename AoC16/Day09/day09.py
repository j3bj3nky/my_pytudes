import re

regex = re.compile(r'[(](\d+)x(\d+)[)]').match


def decompress(s):
    s = re.sub('\s', '', s)
    result = []
    i = 0

    while i < len(s):
        m = regex(s, i)
        if m:
            i = m.end()
            C, R = map(int, m.groups())
            result.append(s[i:i+C] * R)
            i+= C
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)


def decompress_length(s):
    s = re.sub('\s', '', s)
    length = 0
    i = 0

    while i < len(s):
        m = regex(s, i)
        if m:
            i = m.end(0)
            C, R = map(int, m.groups())
            length += R * decompress_length(s[i:i+C])
            i += C
        else:
            length += 1
            i += 1

    return length


data = open('input09.txt').read()
print(len(decompress(data)))
print(decompress_length(data))
