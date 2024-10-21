class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.size += 1

    def print_list(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __iter__(self):
        return LinkedListIterator(self.head)
    def __len__(self):
        """Vrátí počet prvků v seznamu.
           :return:Vraci pocet prvku v podobe cisla
        """
        return self.size


    def __getitem__(self, index):
        """Vrátí prvek na daném indexu.
            :index: Predstavuje pozici pozadovaneho prvku v podobe cisla
            :return:Vraci pocet prvku v podobe cisla

        """
        if index < 0 or index >= self.size or not isinstance(index, int):
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


    def __setitem__(self, index, value):
        """Nastaví hodnotu na daném indexu.
            :index: Predstavuje pozici pozadovaneho prvku v podobe cisla
            :value: Predstavuje hodnotu, ktera se nastavi dannemu prvku
        """
        if index < 0 or index >= self.size or not isinstance(index, int):
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __contains__(self, item):
        """Zkontroluje zda se v listu nachazi danny prvek.
            :item: Predstavuje prvek, ktery je hledan v listu
        """
        current = self.head
        while current:
            if item == current.data:
                return False
            else:
                return True

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

for value in linked_list.print_list():
    print(value)

print("-----iter------")
for i in linked_list:
    print(i)
