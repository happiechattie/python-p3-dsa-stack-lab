class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if self.size() == 0 else False

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)
        else:
            pass

    def pop(self):
        if self.isEmpty():
            pass
        else:
            value = self.items[-1]
            self.items.pop()
            return value

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return False if self.size() == 0 else True

    def search(self, target):
        place = -1
        for i in range(self.size()):
            if target == self.items[i]:
                place = self.size() - i - 1
        return place