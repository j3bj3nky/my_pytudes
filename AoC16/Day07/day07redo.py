# okay I need to totally redo this from scratch.
import re


def split_ip(ip):
    split = re.split(r'\[|\]', ip)

    outside = split[::2]
    inside = split[1::2]

    return outside, inside


def tls(ip):
    outside, inside = split_ip(ip)
    abba_regex = r'(?!(\w)\1\1\1)(\w)(\w)\3\2'
    abba_flag = False

    for o in outside:
        match = re.search(abba_regex, o)
        if match:
            abba_flag = True
            break

    inside_flag = False
    for i in inside:
        match = re.search(abba_regex, i)
        if match:
            inside_flag = True
            break

    if abba_flag and not inside_flag:
        return True
    else:
        return False


print(sum(tls(ip) for ip in open('input07.txt')))
