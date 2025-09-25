#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iter)
            self.counter += 1
            return item
        except StopIteration:
            raise
