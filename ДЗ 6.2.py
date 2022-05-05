import random

l1 = l2 = [random.randint(1, 99) for i in range(random.randint(1, 99))]

l1 = [i for i in l1 if i % 3 == 0]
l2 = [i for i in l2 if i % 5 == 0]

l1, l2 = set(l1), set(l2)

print(list(l1 & l2))
