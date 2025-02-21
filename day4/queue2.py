import sys
class Queue:
    def __init__(self, size=5):
        self.que=[]
        self.size=size
        print('Empty  Queue is created')
    
    def enqueue(self):
        if len(self.que)==self.size:
            print("Stak is full")
            return
        ele=input("enter the element to be pushed: ")
        self.que.insert(0,ele)
    
    def dequeue(self):
        if not self.que:
            print("Queue is empty")
            return
        print(f'Popped element is : {self.que.pop()}')
    
    def display(self):
        if not self.que:
            print("Queue is empty")
            return
        print(self.que[::-1])

class Menu:
    def __init__(self):
        pass
    def get_menu(self,queue):
        menu = {
            1:queue.enqueue,
            2:queue.dequeue,
            3:queue.display,
            4:self.end_of_program
            }
        return menu
        
    def invalid_choice(self):
        print("Invalid choice")

    def end_of_program(self):
        sys.exit("End of program")

    def run_menu(self):
        queue = Queue()
        while True:
            ch=int(input("1.enqueue 2.dequeue 3.display 4.exit: "))
            menu = self.get_menu(queue)
            menu.get(ch, self.invalid_choice)()
menu = Menu()
menu.run_menu()
