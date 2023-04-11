def read_next(*args):
    for el in args:
        for n in el:
            yield n


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
