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

def isStringWellFormed(myString):
    left="(("
    right="}))"
    s = ArrayStack()
    for c in myString:
        if c in left:
            s.push(c)
        elif c in right:
            if s.is_empty():
                return False
            if right.index(c) != left.index(s.pop()):
                return False
    return s.is_empty()
r=isStringWellFormed("((}))")
print(r)
