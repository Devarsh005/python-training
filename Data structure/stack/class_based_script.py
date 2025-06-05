class Stack:
    def __init__(self,size):
        """initialization of stack"""
        self.size = size
        self.data = [None]*self.size
        self.top = -1
    def push(self,new_element):
        if self.is_full():
            raise OverflowError("overflowError :stack is full")
        else:
            self.top = self.top +1 
            self.data[self.top] = new_element
            return
    def pop(self):
        if self.is_empty():
            raise IndexError("IndexError : stack is empty")
        else:
            poped_element = self.data[self.top]
            # self.data[self.top] = None
            self.top -= 1
            return 
    def peak(self):
        return self.data[self.top]
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    def is_full(self):
        if self.top == self.size -1:
            return True
        return False
        








def main():
    
    """main script"""
    stack_size = int(input("enter the size of stack"))
    stack = Stack(stack_size)

    menuSelection = (
    "press integer for operation \n "
    "1: push items \n "
    "2: pop items \n "
    "3: find the Top item \n "
    "4: check isempty \n "
    "5: get size of stack \n "
    "6: check stack is full \n "
    "7: display stack\n "
    "8: exit")
    print(menuSelection)

    flag = True
    while flag:
        choice = input("choose integer from the Menu Selection")
        match choice:
            case "1":
                try:
                    element = input("enter element")
                    stack.push(element)
                    print(f"{element} is pushed")
                except OverflowError as e:
                    print(e)

            case "2":
                try:
                    print(f"{stack.data[stack.top]} is poped")
                    stack.pop()
                except IndexError as e:
                    print(e)
            case "3":
                print(f"top element is {stack.peak()}")
            case "4":
                if stack.is_empty():
                    print("stack is empty")
                else:
                    print("stack is not empty")
            case "5":
                print(f"stack current size is {stack.top+1}")
            case "6":
                if stack.is_full():
                    print("stack is full")
                else:
                    print("stack is not full")
            case "7":
                print(f"stack is {stack.data[:stack.top+1]}")
            case "8":
                flag = False
            case _:
                print("choose between 1 to 8")
    
if __name__ == "__main__":
    main()