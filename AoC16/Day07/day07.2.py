import re
import regex


def segment(line):
    return re.split(r'\[|\]', line)


def split(segments):
    outside = segments[::2]
    inside = segments[1::2]

    return outside, inside


def ssl(segments):
    outs, ins = split(segments)
    ssl_regex = r'(\w)(\w)\1'
    aba_matches = []
    is_ssl = 0
    for o in outs:
        overlapping_matches = regex.findall(ssl_regex, o, overlapped=True)
        if overlapping_matches:
            aba_matches += overlapping_matches
    found = False
    for i in ins:
        for a in aba_matches:
            bab = a[1] + a[0] + a[1]
            if bab in i and a[1] != a[0]:
                found = True
    if found is True:
        is_ssl = 1

    return is_ssl


print(sum(ssl((segment(ip))) for ip in open('input07.txt')))
