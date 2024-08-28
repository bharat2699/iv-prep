import sys

# sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


class DynamicArray:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity  # len of array
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


d_arr = DynamicArray(4)

print(d_arr.arr)
d_arr.set(0, 4)
print(d_arr.size)
print(d_arr.arr)

print(d_arr.get(2))
