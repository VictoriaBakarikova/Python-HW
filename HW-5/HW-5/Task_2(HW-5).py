class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self._last_node is None:
            self._first_node = new_node
            self._last_node = new_node
        else:
            self._last_node.next = new_node
            self._last_node = new_node
        self._size += 1

    def dequeue(self):
        if self._first_node is None:
            raise IndexError('Queue is empty')
        dequeued_data = self._first_node.data
        self._first_node = self._first_node.next
        if self._first_node is None:
            self._last_node = None
        self._size -= 1
        return dequeued_data

    def front(self):
        if self._first_node is None:
            raise IndexError('Queue is empty')
        return self._first_node.data

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def display(self):
        if self._first_node is None:
            print('Queue is empty')
        else:
            current_node = self._first_node
            while current_node:
                print(current_node.data, end=", ")
                current_node = current_node.next
            print("END")

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)

print(queue.front())
queue.display()
print(queue.size())
queue.is_empty()
print(queue.dequeue())


