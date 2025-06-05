      
def create_stack(max_size):
    """Create stack function create a empty list for new stack """
    new_list = [None]*max_size
    return new_list
def get_size(top):
    """return the length of the stack"""
    return top

def is_empty(top):
    """check the stack isempty or not"""
    if top == -1:
        return True
    else:
        return False
def top(top):
    """return the top element of stack"""
    return top
def is_full(top , max_size):
    """check if the stack is full or not"""
    if top == max_size-1:
        return True
    else:
        return False
def push(stack,new_element,top,max_size):
        """add element in the stack at top"""
        if is_full(top,max_size):
            raise OverflowError("Stack is overflow")
        else:
            top = top+1
            stack[top] = new_element
            return top
        
def pop(stack,top_element):
    """remove the element from the stack at the top"""
    if is_empty(top_element):
        raise IndexError("stack is underflow")
    else:
        poped_element = stack[top_element]
        stack[top_element] = None
        top_element -= 1
        return top_element , poped_element
# create naive script here

def main():
    max_size = int(input("enter the size of stack"))
    stack = create_stack(max_size)
    top = -1

    menuSelection = """
    press integer for operation
    1: push items 
    2: pop items
    3: find the Top item
    4: check isempty
    5: get size of stack
    6: check stack is full
    7: display stack
    8: exit
        """
    print(menuSelection)
    flag = True
    while flag:
        select_from_menuselection = input("enter your choice")
        match select_from_menuselection:
            case "1":
                try:
                    element = input("enter element")
                    top  = push(stack,element,top,max_size)
                    print(f"{element} is pushed ")
                except OverflowError as e:
                    print(e)
            case "2":
                try:
                    top , poped_element = pop(stack,top)
                    print(f"{poped_element} is removed")
                except IndexError as e:
                    print(e)
            case "3":
                print(f"Top element at index is :  {stack[top]}")
            case "4":
                if is_empty(top):
                    print("stack is empty")
                else:
                    print("stack is not empty")
            case "5":
                print(f"size of the stack is {get_size(top+1)}")
            case "6":
                if is_full(top,max_size):
                    print("stack is full")
                else:
                    print("stack is not full")
            case "7":
                print(f"stack is {stack[:top+1]}")
            case "8":
                print(f"exit successfully")
                flag = False
            case _:
                print("invalid choice , please select from 1 to 8")
    return

main()

