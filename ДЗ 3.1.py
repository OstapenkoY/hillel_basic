l = [0, 1, 2, 3, 4, 5] 
#l = [1, 3, 5] 
#l = [6] 
#l = [] 
c = 0
if l:
    for i in range(len(l)):
        if i % 2 == 0:
            c += l[i]
    print(c * l[-1])
else:
    print(0)
    

