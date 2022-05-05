def correct_sentence(a):
    if a[0].isupper() == False and a[-1] != '.':
        b = ''.join(list(a)[0].title()) + a[1:] + '.'
        return b
    elif a[0].isupper() == False and a[-1] == '.':
        b = ''.join(list(a)[0].title()) + a[1:]
        return b
    elif a[0].isupper() == True and a[-1] != '.':
        b = a + '.'
        return b
    else:
        return a
        


a = input()

print(correct_sentence(a))

