class dictionary_iter:
    def __init__(self, dict: dict):
        self.dict = tuple(dict.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dict)-1:
            raise StopIteration
        else:
            self.index += 1
            return self.dict[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
