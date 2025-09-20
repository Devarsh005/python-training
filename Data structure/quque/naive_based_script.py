
def main():
    max = int(input("enter the queue size"))
    # creat a empty quque
    queue = [None]*max
    front = 0
    rear = -1
    # item_count = 0
    choice = ("1:push the elemet\n"
              "2: pop the element\n"
              "3:peek element\n"
              "4:isempty\n"
              "5:isfull\n"
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
                    if rear < max-1 :
                        rear = rear + 1
                        queue[rear] = element
                        # item_count += 1
                        print(f"{element} is pushed")
                    else:
                        # rear =-1
                        raise OverflowError("queue is overflow")
                except OverflowError as e:
                    print(e)
            case "2": 
                try:
                    if front < rear:
                        print(f"{queue[front]} is poped")
                        queue[front] = None
                        front = front + 1
                        # item_count -= 1
                    elif front == rear:
                        print(f"{queue[front]} is poped")
                        queue[front] = None
                        front = 0
                        rear = -1
                    else:
                        raise IndexError("queue is underflow")
                except IndexError as e:
                    print(e)
            case "3": 
                print(f"the peek element is {queue[front]}")
            case "4": 
                if front==rear+1:
                    print("queue is empty")
                else:
                    print("queue is not empty")
            case "5":
                if rear==max-1:
                    print(f"queue is full")
                else:
                    print("queue is not full")
            case "6": 
                print(f"queue{queue}  front->{front} rear->{rear}")
            case "7":
                flag = False
            case _:
                print("choose between 1 to 8")
    return

if __name__ == "__main__":
    main()