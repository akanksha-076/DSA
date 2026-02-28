class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data


# Demo
stack = Stack()
stack.push(10)
stack.push(20)
print("Peek:", stack.peek())
print("Pop:", stack.pop())