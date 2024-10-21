
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







class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
        self.size = 0

    def add(self, data):
        self.linked_list.append(data)
        self.size += 1


    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty queue")
        first_node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:  # Pokud je jen jeden prvek
            self.linked_list.head = self.linked_list.tail = None
        else:
            self.linked_list.head = first_node.next
            self.linked_list.head.previous = None
        self.size -= 1
        return first_node.data


    def count(self):
        return self.size


    def clear(self):
        self.linked_list.head = self.linked_list.tail = None
        self.size = 0


    def popAll(self):
        elements = []
        while self.size > 0:
            elements.append(self.pop())
        return str(elements)



queue = Queue()
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)
queue.add(50)


print("Počet prvků ve frontě:", queue.count())

try:
    print("Odebraný prvek:", queue.pop())
except IndexError:
    print("!")


print("Počet prvků po pop:", queue.count())


print("Všechny prvky z fronty:", queue.popAll())


print("Počet prvků po popAll:", queue.count())
