x = int(input())

x, a = divmod(x, 10)
x, b = divmod(x, 10)
x, c = divmod(x, 10)
x, d = divmod(x, 10)
x, e = divmod(x, 10)

print(int(str(a) + str(b) +str(c) + str(d) + str(e)))
