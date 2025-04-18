class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackIterator:
    def __init__(self, stack):
        self.current_node = stack._top_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next
        return data


class Stack:
    def __init__(self):
        self._top_node = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top_node
        self._top_node = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        removed_item = self._top_node.data
        self._top_node = self._top_node.next
        self._size -= 1
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._top_node.data

    def is_empty(self):
        return self._top_node is None

    def size(self):
        return self._size

    def display(self):
        current_node = self._top_node
        current_nodes = []
        while current_node:
            current_nodes.append(current_node.data)
            current_node = current_node.next
        print("Stack:", ", ".join(map(str, current_nodes)))

    def __iter__(self):
        return StackIterator(self)


stack = Stack()
stack.push(23)
stack.push(5)
stack.push(76)
stack.push(24)
stack.push(34)

stack.display()
print(stack.pop())
print(stack.pop())
print(stack.peek())

for item in stack:
    print(item)