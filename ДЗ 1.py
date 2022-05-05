x = int(input())


#print(x%10000//1000)
#print(x%1000//100)
#print(x%100//10)
#print(x%10)

#С использованием функции divmod()

one, _ = divmod(x, 1000)
two, _ = divmod(x%1000, 100)
three, _ = divmod(x%100, 10)
four, _ = divmod(x%10, 1)

print(one)
print(two)
print(three)
print(four)






