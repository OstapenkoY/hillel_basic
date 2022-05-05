def f(a, n):
    if a.count(n) >= 2:
        l = a.split(n)
        s = [len(i) for i in l]
        i = s[0] + s[1] + 1
        return i
    else:
        return 

a = input()
n = input()

print(f(a,n))
