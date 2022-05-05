def fun_inc(x, y):
    if x > y:
        raise ValueError
    else:
        return x

def fun_dec(x, y):
    if x < y:
        raise ValueError
    else:
        return x

class Counter:

    def __init__(self, min, max, start):
        self.min = min
        self.max = max
        self.start = start
        self.current = 0

    def inc(self):
        try:
            self.current += 1
            z = fun_inc(self.current + self.start, self.max)
            return z
        except ValueError:
            self.current -= 1
            return 'Maximum reached'

    def dec(self):
        try:
            self.current -= 1
            z = fun_dec(self.current + self.start, self.min)
            return z
        except ValueError:
            self.current += 1
            return 'Minimum reached'

    def curr(self):
        return self.current + self.start



my_count=Counter(1, 6, 3)

print(my_count.inc())
print(my_count.inc())
print(my_count.inc())
print(my_count.inc())
print(my_count.dec())
print(my_count.dec())
print(my_count.dec())
print(my_count.dec())
print(my_count.dec())
print(my_count.dec())
print(my_count.inc())
print(my_count.inc())
print(my_count.curr())
print(my_count.inc())
print(my_count.inc())
print(my_count.inc())
print(my_count.curr())
print(my_count.inc())
print(my_count.curr())
























