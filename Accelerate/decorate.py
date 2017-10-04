@jit(nogil=True)
def my_calc(x, y, z):
    for i in range(x):
        w = z * y + i
        q = my_other_calc(w)

@jit(nopython=True)
def my_other_calc(w):
    w = w*7
    return w


@jit(nopython=True)
def add(a, b):
    return a+b

add(7, 8)
add(7.8, 9)
add(7+8i, 10)

# This PROBABLY blow up because of nopython=True
add(Fraction(1,7), Fraction(1,8))

class MyFunnyNumber(Fraction):
    def __add__(self, other):
        # do somthing
        return 42

# This will blow up in the nopython function!!!
add(MyFunnyNumber(3), MyFunnyNumber(2))

