# Importing necessary modules for performance and random value tests
import random
import time
import unittest

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

            self.tail.next = new_node

            new_node.previous = self.tail

            self.tail = new_node



    def print_list_forward(self):

        current = self.head

        while current:

            yield current.data

            current = current.next



    def print_list_backward(self):

        current = self.tail

        while current:

            yield current.data

            current = current.previous

# Updated tests with performance and inclusion checks
class TestLinkedListExtended(unittest.TestCase):
    def test_initialization(self):
        # Test initial state of LinkedList
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_append_single(self):
        ll = LinkedList()
        ll.append(10)
        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.tail.data, 10)
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.head.previous)

    def test_append_multiple(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.tail.data, 30)
        self.assertEqual(ll.head.next.data, 20)
        self.assertEqual(ll.tail.previous.data, 20)

    def test_print_list_forward(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        output = list(ll.print_list_forward())
        self.assertEqual(output, [10, 20, 30])

    def test_print_list_backward(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        output = list(ll.print_list_backward())
        self.assertEqual(output, [30, 20, 10])

    def test_element_in_list(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)

        # Test element presence
        self.assertIn(20, list(ll.print_list_forward()))
        self.assertNotIn(40, list(ll.print_list_forward()))

    def test_performance_large_insertion(self):
        ll = LinkedList()

        # Insert 1 million random values between 1 and 999
        values = [random.randint(1, 999) for _ in range(1_000_000)]
        for value in values:
            ll.append(value)

        # Measure the time taken to count occurrences of 186
        start_time = time.time()
        count = sum(1 for value in ll.print_list_forward() if value == 186)
        end_time = time.time()

        # Assert that the operation is within 500 milliseconds
        self.assertTrue(end_time - start_time <= 0.5, "Counting operation took too long!")

        # Print the count for debugging
        print(f"Count of 186: {count}")


# Running the extended tests
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestLinkedListExtended))