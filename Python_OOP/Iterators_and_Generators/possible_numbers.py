from itertools import permutations


def possible_permutations(param):
    for item in permutations(param):
        yield list(item)






[print(n) for n in possible_permutations([1, 2, 3])]