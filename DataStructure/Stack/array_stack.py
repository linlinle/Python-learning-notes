# -*- coding: utf-8 -*-

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()
