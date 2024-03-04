class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = None
        self.size = 0

    def add_to_stack(self, item):
        if self.is_full():
            raise MyOutOfSizeException("La pile est pleine, impossible d'ajouter un nouvel élément.")
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("La pile est vide, impossible de récupérer un élément.")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    myStack = MyStack(3)
    myStack.add_to_stack('hello')
    myStack.add_to_stack('world')
    print(myStack.is_full()) # False
    myStack.add_to_stack('!')
    print(myStack.is_full()) # True
    try:
        myStack.add_to_stack('extra') # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)

    print(myStack.pop_from_stack()) # !
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # world
    print(myStack.is_empty()) # False
    print(myStack.pop_from_stack()) # hello
    print(myStack.is_empty()) # True
    try:
        print(myStack.pop_from_stack()) # MyEmptyStackException
    except MyEmptyStackException as e:
        print(e)
