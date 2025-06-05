def push(deque,element,front,rear,size):
    if is_full(front,rear,size):
        raise OverflowError("deque is overflow")
    elif is_empty(front):
        front = 0
        rear = 0
    elif rear == size-1:
        rear = 0
    else:
        rear += 1
    deque[rear] = element
    return deque , front ,rear
def push_left(deque,element,front,rear,size):
    if is_full(front,rear,size):
        raise OverflowError("deque is overflow")
    elif is_empty(front):
        front = 0
        rear = 0
    elif front == 0:
        front = size -1
    else:
        front -= 1
    deque[front] = element
    return deque , front ,rear
def pop(front,rear,size):
    if is_empty(front):
        raise IndexError("deque underflow")
    elif front == rear:
        front,rear = -1,-1
    elif rear == 0:
        rear = size -1
    else:
        rear -= 1
    return front ,rear
def pop_left(front,rear,size):
    if is_empty(front):
        raise IndexError("deque underflow")
    elif front == rear:
        front,rear = -1,-1
    elif front == size -1:
        front = 0
    else:
        front += 1
    return front ,rear
def is_full(front,rear,size):
    if front == 0 and rear == size-1 or (front == rear+1):
        return True
    return False
def is_empty(front):
    if front == -1:
        return True
    return False


def main():
    size = int(input("enter the size of deque"))
    deque = [None]*size
    choice = ("1:push the elemet\n"
               "2:push the elemet at front\n"
              "3: pop the element\n"
              "4: pop the element at front\n"
              "5:isfull\n"
              "6:isempty\n"
              "7:display the queue\n"
              "8:close\n")
    print(choice)
    flag = True
    front = -1
    rear = -1
    while flag:
        choice = input("choose operation")
        match choice:
            case "1" :
                try:
                    element = input("enter the element")
                    deque,front,rear =  push(deque,element,front,rear,size)
                    print(f"{element} is pushed")
                except OverflowError as e:
                    print(e)
            case "2":
                try:
                    element = input("enter the element")
                    deque , front , rear = push_left(deque,element,front,rear,size)
                except OverflowError as e:
                    print(e)
            case "3":
                try:
                    front , rear = pop(front,rear,size)
                except IndexError as e:
                    print(e)
            case "4":
                try:
                    front , rear = pop_left(front,rear,size)
                except IndexError as e:
                    print(e)
            case "5":
                if is_full(front,rear,size):
                    print("deque is full")
                else:
                    print('deque is not full')
            case "6":
                if is_empty(front):
                    print("deque is empty")
                else:
                    print("deque is not empty")
            case "7":
                print(f"deque is {deque} front ->{front} rear ->{rear}")
            case "8":
                flag = False
            case _:
                print("choose between 1 to 9")
if __name__ =="__main__":
    main()