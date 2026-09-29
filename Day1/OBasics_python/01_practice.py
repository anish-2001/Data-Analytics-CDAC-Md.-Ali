from functools import partial
def fun(a, b, c, x):
    return a+b+c+x

print(fun(1, 2, 3, 4))

g = partial(fun, 10, 20, 30)

print(g(100))

print("_" * 60)

def greet(msg):
    def inner(sep):
        def inner_most(name):
            return f"{msg}{sep}{name}"
        return inner_most
    return inner

