class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        else:
            self.count -= 1
            self.num += self.step
            return self.num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
