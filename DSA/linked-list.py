# Node class
class Node:
    def __init__(self, data):
        self.data = data      # value store karega
        self.next = None      # next node ka reference


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None      # starting node


    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # Delete a node
    def delete(self, key):
        temp = self.head

        # If head contains the key
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


    # Search element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------
# Main Program
# -------------------------

ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()

print("Search 20:", ll.search(20))

ll.delete(20)

ll.display()