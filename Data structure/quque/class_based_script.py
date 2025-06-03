class Queue:
    def __init__(self,size):
        self.size = size
        self.data = [None]*self.size
        self.front = 0
        self.rear = -1
        # self.item_count = 0

    def push(self,element):
        if not self.is_full():
            self.rear += 1
            self.data[self.rear] = element
            # self.item_count += 1    
            print(f"{element} is pushed")     
        else:
            # self.rear = 0
            raise OverflowError("queue is overflow")
        
    def pop(self):
        if not self.is_empty() and self.front < self.rear:
            print(f"{self.data[self.front]} is popped")
            self.data[self.front] = None
            self.front += 1
            # self.item_count -= 1
        elif self.front == self.rear:
            print(f"{self.data[self.front]} is popped")
            self.data[self.front] = None
            self.front = 0
            self.rear = -1
        else:
            # self.front = 0
            raise IndexError("queue is underflow")
        
    def is_full(self):
        if self.rear == self.size-1:
            return True
        return False
    def is_empty(self):
        if self.front == self.rear+1:
            return True
        else:
            return False
    def peek(self):
        return self.data[self.front]
def main():
    max = int(input("enter the size of queue"))
    queue = Queue(max)
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
                    queue.push(element)
                except OverflowError as e:
                    print(e)

            case "2": 
                try:
                    queue.pop()
                except IndexError as e:
                    print(e)

            case "3": 
                print(f"the peek element is {queue.peek()}")

            case "4": 
                if queue.is_full():
                    print("queue is full")
                else:
                    print("queue is not full")

            case "5":
                if queue.is_empty():
                    print(f"queue is empty")
                else:
                    print("queue is not empty")

            case "6": 
                print(f"queue{queue.data} front ->{queue.front} rear ->{queue.rear}")

            case "7":
                flag = False
                
            case _:
                print("choose between 1 to 8")
    return

if __name__ == "__main__":
    main()

