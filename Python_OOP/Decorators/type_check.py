def type_check(tag):

    def check_fun(fun):
        def wrapper(param):
            if isinstance(param, tag):
                return fun(param)
            return "Bad Type"
        return wrapper
    return check_fun


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

