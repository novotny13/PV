
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            self.tail = new_node
            new_node.previous = last


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

        current = self.tail
        while current:
               yield current.data
            current = current.next



linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)


for value in linked_list.print_list():
    print(value)
