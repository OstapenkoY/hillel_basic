def common_div(ch, zn):
    while ch % zn != 0:
        ch, zn = zn, ch % zn
    return zn

class Proper_fraction:

    def __init__(self, a, b, c = 0):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.c != 0:
            return f'{self.c} {self.a}/{self.b}'
        else:
            if self.a == self.b:
                return f'{1}'
            elif self.a == 0:
                return f'{0}'
            return f'{self.a}/{self.b}'

    def __add__(self, other):
        ch = self.a * other.b + other.a * self.b
        zn = self.b * other.b
        common = common_div(ch, zn)
        if (ch // common) > (zn // common):
            cel = (ch // common) // (zn // common)
            ch = (ch // common) % (zn // common)
            zn = (zn // common)
            return Proper_fraction(ch, zn, cel)
        else:
            return Proper_fraction(ch // common, zn // common)

    def __mul__(self, other):
        ch = self.a * other.a
        zn = self.b * other.b
        common = common_div(ch, zn)
        return Proper_fraction(ch // common, zn // common)

    def __sub__(self, other):
        ch = self.a * other.b - other.a * self.b
        zn = self.b * other.b
        common = common_div(ch, zn)
        if (ch // common) > (zn // common):
            cel = (ch // common) // (zn // common)
            ch = (ch // common) % (zn // common)
            zn = (zn // common)
            return Proper_fraction(ch, zn, cel)
        elif (ch // common) == 0:
            return Proper_fraction(ch, zn)
        else:
            return Proper_fraction(ch // common, zn // common)

    def __gt__(self, other):
        if self.b == other.b and self.a != other.a:
            return self.a > other.a
        elif self.a == other.a and self.b != other.b:
            return self.b < other.b
        else:
            ch1 = self.a * other.b
            ch2 = other.a * self.b
            return ch1 > ch2


fr1 = Proper_fraction(1, 3)
fr2 = Proper_fraction(1, 3)
print(fr1)
print(fr2)
fr3 = fr1 + fr2
print(fr3)
print(fr1 < fr2)