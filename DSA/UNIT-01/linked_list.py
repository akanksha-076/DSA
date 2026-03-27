
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
    def delete(self, key):

        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None


    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print("Value found at position", position)
                return
            temp = temp.next
            position += 1

        print("Value not found")
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Linked List:")
ll.display()

print("\nSearching 30:")
ll.search(30)

print("\nDeleting 20:")
ll.delete(20)

print("\nLinked List after deletion:")
ll.display()