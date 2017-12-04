def op(fn):
    return MyOperator(fn)

# TODO first assume other is primitive, then fall back to assuming other is operator
# TODO make sure eg. radd and all other are implemented.
class MyOperator:
    def __init__(self, f): self.f = f
    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
    def __add__(self, other):
        return MyOperator(lambda *args: self.f(*args) + (other if type(other) != MyOperator else other.f(*args)))
    def __radd__(self, other):
        return MyOperator(lambda *args: (other if type(other) != MyOperator else other.f(*args)) + self.f(*args))
    def __sub__(self, other):
        return MyOperator(lambda *args: self.f(*args) - other.f(*args))
    def __mul__(self, other):
        return MyOperator(lambda *args: self.f(*args) * (other if type(other) != MyOperator else other.f(*args)))
    def __rmul__(self, other):
        return MyOperator(lambda *args: (other if type(other) != MyOperator else other.f(*args)) * self.f(*args) )
    def __contains__(self, other):
        return MyOperator(lambda *args: self.f(*args) in other.f(*args))
    def __truediv__(self, other):
        return MyOperator(lambda *args: self.f(*args) / other.f(*args))
    def __floordiv__(self, other):
        return MyOperator(lambda *args: self.f(*args) // other.f(*args))
    def __and__(self, other):
        return MyOperator(lambda *args: self.f(*args) & other.f(*args))
    def __xor__(self, other):
        return MyOperator(lambda *args: self.f(*args) ^ other.f(*args))
    def __invert__(self):
        return MyOperator(lambda *args: ~ self.f(*args))
    def __or__(self, other):
        return MyOperator(lambda *args: self.f(*args) | other.f(*args))
    def __pow__(self, other):
        return MyOperator(lambda *args: self.f(*args) ** other.f(*args))
    def __is__(self, other):
        return MyOperator(lambda *args: self.f(*args) is other.f(*args))
    def __is_not__(self, other):
        return MyOperator(lambda *args: self.f(*args) is not other.f(*args))
    def __is__(self, other):
        return MyOperator(lambda *args: self.f(*args) is other.f(*args))
    def __setitem__(self, k, v):
        return lambda *args: self.f(*args).__setitem__(k, v)
    def __delitem__(self, k):
        return lambda *args: self.f(*args).__delitem__(k)
    def __getitem__(self, k):
        return lambda *args: self.f(*args).__getitem__(k)

@op
def inc(x):
    return x + 1

@op
def double_of_inc(x):
    return (inc + inc)(x)

max, min = op(max), op(min)
#print((max - min) ([1, 2, 3, 4]))

x = op(lambda x: x)

poly = x*x + 2*x + 1

roots = filter(lambda x: abs(poly(x)) < .00001, (.01 * e for e in range(-500, 500)))
#print([*roots])

first_name = op(lambda x: x)
last_name = op(lambda x: x)

#print((first_name + " " + last_name) ('foobar'))

#obj[k]	getitem(obj, k)
#Shift	a << b	lshift(a, b)
#a % b	mod(a, b)
#a * b	mul(a, b)
#Multiplication	a @ b	matmul(a, b)
#Arithmetic)	- a	neg(a)
#Logical)	not a	not_(a)
#a	pos(a)
#Shift	a >> b	rshift(a, b)
#Assignment	seq[i:j] = values	setitem(seq, slice(i, j), values)
#Deletion	del seq[i:j]	delitem(seq, slice(i, j))
#seq[i:j]	getitem(seq, slice(i, j))
#Formatting	s % obj	mod(s, obj)
#a - b	sub(a, b)
#Test	obj	truth(obj)
#a < b	lt(a, b)
#a <= b	le(a, b)
#a == b	eq(a, b)
#a != b	ne(a, b)
#a >= b	ge(a, b)
#a > b	gt(a, b)
