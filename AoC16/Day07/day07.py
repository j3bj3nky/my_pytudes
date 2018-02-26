# okay this one is tricky.  Gotta find the number of 'TLS' supporting IPs
# this will take many loops and if...else statements.  Maybe I can split into
# different functions.  I doubt it.

# might need to be a greater loop


STRING = ''
TLS = 0
NOT_TLS = False
A = 0
B = 1
C = 2
D = 3


def bracket_check(brack_line):
    # then I have to check for brackets. Maybe do this first?
    a = A
    b = B
    c = C
    d = D
    string = STRING
    global NOT_TLS
    NOT_TLS = False
    if brack_line.find('[') and brack_line.find(']'):
        brack1 = brack_line.find('[')
        brack2 = brack_line.find(']')
        for lett in range(brack1, brack2):
            lett1 = brack_line[a]
            lett2 = brack_line[b]
            lett3 = brack_line[c]
            lett4 = brack_line[d]
            if lett1 + lett2 == lett4 + lett3:
                in_between = (lett1+lett2+lett4+lett3)
                if in_between == string:
                    NOT_TLS = True
                    break
            a += 1
            b += 1
            c += 1
            d += 1
            if d == brack_line[-1]:
                break


def tls_check(check_line):
    global NOT_TLS
    global STRING
    a = A
    b = B
    c = C
    d = D
    NOT_TLS = False
    for x in range(len(check_line)):
        lett1 = check_line[a]
        lett2 = check_line[b]
        lett3 = check_line[c]
        lett4 = check_line[d]
        if lett1 + lett2 == lett3 + lett4:
            # second if statement
            if lett1 != lett2:
                NOT_TLS = False
                STRING = (lett1+lett2+lett4+lett3)
                break
            else:
                NOT_TLS = True
                break

        a += 1
        b += 1
        c += 1
        d += 1
        if d == check_line[-1]:
            break


def reader(file):
    global TLS
    f = open(file, 'r')
    for x in range(len(file)):
        cur_line = f.readline()
        cur_line = cur_line.rstrip()
        tls_check(cur_line)
        if NOT_TLS is False:
            bracket_check(cur_line)
            if NOT_TLS is False:
                TLS += 1

    f.close()


reader('input07.txt')
