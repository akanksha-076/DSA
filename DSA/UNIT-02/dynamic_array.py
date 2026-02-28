class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        self.arr[self.size] = value
        self.size += 1

    def resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return
        self.size -= 1
        value = self.arr[self.size]
        self.arr[self.size] = None
        return value

    def display(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


# Demo
da = DynamicArray()
da.append(10)
da.append(20)
da.append(30)
da.display()
print("Popped:", da.pop())
da.display()