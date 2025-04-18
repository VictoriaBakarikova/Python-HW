class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.size = 0

    def append(self, item):
        new_node = Node(item)
        if self.tail_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            new_node.prev = self.tail_node
            self.tail_node = new_node
        self.size += 1

    def prepend(self, item):
        new_node = Node(item)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.head_node.prev = new_node
            new_node.prev = self.head_node
            self.head_node = new_node
        self.size += 1

    def insert(self, item, i):
        if i < 0 or i > self.size:
            raise IndexError('Index out of range')
        if i == 0:
            self.prepend(item)
        elif i == self.size:
            self.append(item)
        else:
            new_node = Node(item)
            current_node = self.head_node
            for _ in range(i - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            if current_node.next:
                current_node.next.prev = new_node
            current_node.next = new_node
            self.size += 1

    def delete(self, item):
        current_node = self.head_node
        while current_node:
            if current_node.data == item:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head_node = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail_node = current_node.prev
                self.size -= 1
                return
            current_node = current_node.next
        raise ValueError("Item doesn't found in the list")

    def find(self, item):
        current_node = self.head_node
        while current_node:
            if current_node == item:
                return current_node
            else:
                current_node = current_node.next
        return

    def display(self, reverse=True):
        if reverse:
            current_node = self.head_node
            while current_node:
                print(current_node.data, end=";")
                current_node = current_node.next
        else:
            current_node = self.tail_node
            while current_node:
                print(current_node.data, end=";")
                current_node = current_node.prev
        print("None")

    def __getitem__(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        current_node = self.head_node
        for _ in range(i):
            current_node = current_node.next
        return current_node.data

    def size(self):
        return self.size

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.insert(1, 4)

linked_list.display()
linked_list.delete(7)
linked_list.display()
linked_list.find(7)
