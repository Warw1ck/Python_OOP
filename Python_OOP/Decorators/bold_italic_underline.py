def make_bold(fun):
    def wrapper(*names):
        return f'<b>{fun(*names)}</b>'

    return wrapper


def make_italic(fun):
    def wrapper(*names):
        return f'<i>{fun(*names)}</i>'

    return wrapper


def make_underline(fun):
    def wrapper(*names):
        return f'<u>{fun(*names)}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

