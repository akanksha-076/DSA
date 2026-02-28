class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Demo
dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.display_forward()
dll.display_backward()