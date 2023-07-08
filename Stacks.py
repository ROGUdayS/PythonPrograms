class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def top(self):
        return self.items[len(self.items)-1]
    def push(self, item):
        self.items.append(item)
        print("Control Exists with ", self.top())
    def pop(self):
        popped = self.items.pop()
        print("Control has been returned to ", self.top())
        return popped
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
class Verification:
    return_address_list = []
    def __init__(self):
        print(" -- Verifying Object Instantized -- ")
    def main(self):
        call(self, return_address_list.index("F1"))
        call(self, return_address_list.index("F2"))
    def Func1(self):
        print("Inside Function 1")
        print("Exiting Function 1 .....")
        return
    def Func2(self):
        print("Inside Function 2")
        print("Calling Function 3.....")
        call(self, return_address_list.index("F3"))
        print("Exiting Function 2 .....")
        return
    def Func3(self):
        print("Inside Function 3")
        print("Calling Function 4.....")
        call(self, return_address_list.index("F4"))
        print("Exiting Function 3 .....")
        return
    def Func4(self):
        print("Inside Function 4")
        print("Exiting Function 4 .....")
        return
def call(Verification_Obj, address):
    input(" Enter a key to proceed :")
    if address == 0:
        control.push(return_address_list[address])
        return_val = Verification_Obj.main()
        control.pop()
        return return_val
    elif address == 1:
        control.push(return_address_list[address])
        return_val = Verification_Obj.Func1()
        control.pop()
        return return_val
    elif address == 2:
        control.push(return_address_list[address])
        return_val = Verification_Obj.Func2()
        return return_val
    elif address == 3:
        control.push(return_address_list[address])
        return_val = Verification_Obj.Func3()
        control.pop()
        return return_val
    elif address == 4:
        control.push(return_address_list[address])
        return_val = Verification_Obj.Func4()
        control.pop()
        return return_val
    else:
        raise Exception("Invalid return address, System Error")

if __name__ == "__main__":
    control = Stack()
    print("Control Exists with the System")
    Verification = Verification()
    return_address_list = ["Main", "F1", "F2", "F3", "F4"]
    call(Verification, return_address_list.index("Main"))
    print("End of Verification")
    print("Control is Handed back to the System")