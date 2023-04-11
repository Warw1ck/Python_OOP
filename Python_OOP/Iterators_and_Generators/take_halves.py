def solution():

    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        numbers = []
        for num in seq:
            if len(numbers) >= n:
                break
            numbers.append(num)
        return numbers

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
