class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity

    def get(self, i: int) -> int:
        return self.storage[i]

    def set(self, i: int, n: int) -> None:
        self.storage[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.storage[self.size] = n
        self.size += 1

    def popback(self) -> int:
        value = self.storage[self.size - 1]
        self.size -= 1

        return value

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_storage = [None] * new_capacity

        for i in range(self.size):
            new_storage[i] = self.storage[i]

        self.capacity = new_capacity
        self.storage = new_storage

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
