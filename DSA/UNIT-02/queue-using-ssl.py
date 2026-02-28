class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data


# Demo
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Peek:", q.peek())
print("Dequeue:", q.dequeue())