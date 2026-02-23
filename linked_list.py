
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class 
class LinkedList:
    def __init__(self):
        self.head = None


    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse till last node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # Delete a node by value
    def delete(self, key):

        temp = self.head

        # If head needs to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if temp is None:
            print("Value not found")
            return

        # Remove node
        prev.next = temp.next
        temp = None


    # Search operation
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


    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------------------------
# Testing the Linked List
# ---------------------------------

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