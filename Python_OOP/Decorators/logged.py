def logged(fun):
    def wrapped(*args):
        x = fun(*args)
        return f'you called {fun.__name__}{tuple(args)}\nit returned {x}'
    return wrapped


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

