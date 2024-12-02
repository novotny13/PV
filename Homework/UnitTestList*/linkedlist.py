class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def __contains__(self, item):
        """
        Allows using 'in' to check if an item is in the linked list.
        """
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def count(self, value):
        """
        Counts the occurrences of a given value in the linked list.
        """
        current = self.head
        count = 0
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count
