def fibonacci():
    n = 0
    next_number = 0

    while True:
        yield next_number
        if next_number == 0:
            next_number = 1
        else:
            next_number += n
            n = next_number - n




generator = fibonacci()
for i in range(5):
    print(next(generator))
