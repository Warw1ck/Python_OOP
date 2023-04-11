def tags(tag):
    def decorator(fun):
        def wrapper(*args):
            return f'<{tag}>{fun(*args)}</{tag}>'

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
