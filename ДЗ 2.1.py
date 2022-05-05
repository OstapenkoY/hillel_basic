#x = [1, 2, 3, 4, 5, 6, 7, 8]
#x = []
#x = [1]
x = [1, 2, 3, 4, 5]
y = []
if len(x) % 2 == 0:
    y.append(x[:len(x) // 2])
    y.append(x[len(x) // 2:])
    print(y)
else:
    y.append(x[:(len(x) // 2) + 1])
    y.append(x[(len(x) // 2) + 1:])
    print(y)

