import random

lst = [random.randint(1, 10) for i in range(random.randint(3, 10))]
new_lst = [lst[0], lst[2], lst[-2]]

#print(lst)
print(new_lst)
