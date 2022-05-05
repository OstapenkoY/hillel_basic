#l = [0, 1, 0, 3, 12] 
#l = [0] 
l = [1, 0, 3, 0, 0, 0, 5] 

for i in l:
    if i==0:
        l.append(l.pop(l.index(i)))
print(l)

    

