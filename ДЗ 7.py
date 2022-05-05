def add_one(l):
    l = int(''.join([str(i) for i in l])) + 1
    l = [int(i) for i in list(str(l))]
    return l

print(add_one(l))
    
    
