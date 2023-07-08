class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def push(self,e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.data.pop()

s=ArrayStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.pop())
print(s.is_empty())
print(s.top())
print(len(s))
print(s.data)