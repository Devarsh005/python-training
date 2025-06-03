class Deque:
    def __init__(self,size):
        self.size = size
        self.data = [None]*self.size
        self.front = -1
        self.rear = -1
    def is_full(self):
        if self.front == 0 and self.rear == self.size-1 or (self.front == self.rear+1):
            return True
        else:
            return False
    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False
    def push_left(self,element):
        if self.is_full():
            raise OverflowError
        elif self.is_empty():
            self.front =0
            self.rear =0
        elif self.front == 0:
            self.front = self.size -1
        else:
            self.front -= 1
        self.data[self.front] = element
    def push(self,element):
        if self.is_full():
            raise OverflowError
        elif self.is_empty():
            self.front =0
            self.rear =0
        elif self.rear == self.size -1:
            self.rear = 0
        else:
            self.rear = self.rear +1 
        self.data[self.rear] = element
    def pop(self):
        if self.is_empty():
            raise IndexError("underflow condition")
        elif self.front == self.rear :
            self.front,self.rear = -1,-1
        elif self.rear == 0:
            self.rear = self.size -1
        else:
            self.rear -= 1
    def pop_left(self):
        if self.is_empty():
            raise IndexError("deque underflow")
        elif self.front == self.rear:
            self.front,self.rear = -1,-1
        elif self.front == self.size -1:
            self.front = 0
        else:
            self.front += 1
        

def main():
    max = int(input("enter the size of queue"))
    queue = Deque(max)
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
    while flag:
        choice = input("choose operation")
        match choice:
            case "1" :
                try:
                    element = input("enter the element")
                    queue.push(element)
                    print(f"{element} is pushed")
                except OverflowError as e:
                    print(e)
            case "2":
                try:
                    element = input("enter the element")
                    queue.push_left(element)
                except OverflowError as e:
                    print(e)
            case "3":
                try:
                    queue.pop()
                except IndexError as e:
                    print(e)
            case "4":
                try:
                    queue.pop_left()
                except IndexError as e:
                    print(e)
            case "5":
                if queue.is_full():
                    print("deque is full")
                else:
                    print('deque is not full')
            case "6":
                if queue.is_empty():
                    print("deque is empty")
                else:
                    print("deque is not empty")
            case "7":
                print(f"deque is {queue.data} front ->{queue.front} rear ->{queue.rear}")
            case "8":
                flag = False
            case _:
                print("choose between 1 to 9")
if __name__ == "__main__":
    main()