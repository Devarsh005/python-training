
def push(queue,element,front,rear,max):
    if rear < max-1:
        rear = rear +1 
        queue[rear] = element
        # item_count +=1
        print(f"{element} is pushed")
        return front,rear
    else:
        raise OverflowError("queue is not able to inserted either front == rear")
    
def pop(queue,front,rear):
    if front < rear:
        print(f"{queue[front]} is poped")
        queue[front] = None
        front += 1
        # item_count -= 1
        return front,rear
    elif front == rear:
        print(f"{queue[front]} is poped")
        queue[front] = None
        front = 0
        rear = -1
        return front,rear
    else:
        raise IndexError("queue is underflow")

def is_full(rear,max):
    if rear == max-1:
        return True
    else:
        return False
    
def is_empty(front,rear):
    if front == rear+1:
        return True 
    else:
        return False
def peek(queue , front):
    return queue[front]

def main():
    max = int(input("enter the size of queue"))
    queue = [None]*max
    front = 0
    rear = -1
    # item_count = 0
    choice = ("1:push the elemet\n"
              "2: pop the element\n"
              "3:peek element\n"
              "4:isfull\n"
              "5:isempty\n"
              "6:display the queue\n"
              "7:close\n")
    print(choice)

    flag = True
    while flag:
        choice = input("choose operation")
        match choice:
            case "1":
                try:
                    element = input("enter element")
                    if not is_full(rear,max):
                        front,rear = push(queue,element,front,rear,max)
                    else:
                        raise OverflowError("queue is overflow")
                except OverflowError as e:
                    print(e)

            case "2": 
                try:
                    if not is_empty(front,rear):
                        front,rear = pop(queue,front,rear)
                    else:
                        raise IndexError("queue is underflow")
                except IndexError as e:
                    print(e)

            case "3": 
                print(f"the peek element is {peek(queue,front)}")

            case "4": 
                if is_full(rear,max):
                    print("queue is full")
                else:
                    print("queue is not full")

            case "5":
                if is_empty(front,rear):
                    print(f"queue is empty")
                else:
                    print("queue is not empty")

            case "6": 
                print(f"queue{queue} , front->{front} rear-> {rear}")

            case "7":
                flag = False
                
            case _:
                print("choose between 1 to 8")
    return

    ...
if __name__ == "__main__":
    main()