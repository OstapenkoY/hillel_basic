import keyword
import string

forb_words = keyword.kwlist

inp = input()

if len(inp) == 0 or inp in forb_words:
    print(False)
elif inp[0] in string.digits:
    print(False)
else:
    l = ''
    for i in inp:
        if i in string.digits + '_':
            l += i
        elif i == i.upper():
            continue
        else:
            l += i

    if l == inp:
        print(True)
    else:
        print(False)


