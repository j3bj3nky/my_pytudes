import re
from collections import Counter


# jk first thing is to open file
# I should make an opening function...

# the first thing to do is parse the lines. From what I saw from other
# solutions the best way to do this is with a regex.
def parse(line):
    regex = re.compile(r'(.+)-(\d+)\[([a-z]+)\]')
    return re.match(regex, line).groups()


# splits the line into the three parts needed to evaluate
def sector(line):
    name, sector, checksum = parse(line)
    return int(sector) if valid(name, checksum) else 0


def valid(name, checksum):
    counts = Counter(name.replace('-', ''))
    letters = sorted(counts, key=lambda x: (-counts[x], x))
    return checksum == ''.join(letters[:5])


assert  parse('aaaaa-bbb-z-y-x-123[abxyz]') == ('aaaaa-bbb-z-y-x', '123', 'abxyz')
assert sector('aaaaa-bbb-z-y-x-123[abxyz]') == 123
assert  valid('aaaaa-bbb-z-y-x', 'abxyz')

print(sum(map(sector, open('sectorIDs.txt'))))


def decrypt(line):
    name, sector, _ = parse(line)
    return shift(name, int(sector)) + ' ' + sector


def shift(text, N, alphabet='abcdefghijklmnopqrstuvwxyz'):
    N = N % len(alphabet)
    tr = str.maketrans(alphabet, alphabet[N:] +alphabet[:N])
    return text.translate(tr)


def grep(pattern, lines):
    for line in lines:
        if re.search(pattern, line):
            print(line)


grep('north', map(decrypt, open('cryptoInput.txt')))
