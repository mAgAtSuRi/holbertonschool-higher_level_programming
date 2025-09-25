#!/usr/bin/python3


class VerboseList(list):
    def append(self, object):
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        element_added = 0
        for i in range(len(iterable)):
            element_added += 1
        print(f"Extended the list with [{element_added}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        super().pop(index)
