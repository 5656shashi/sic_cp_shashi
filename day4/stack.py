import sys
class Stack:
    def __init__(self, size=5):
        self.stk=[]
        self.size=size
        print('Empty Stack is created')
    
    def push(self):
        if len(self.stk)==self.size:
            print("Stak is full")
            return
        ele=input("enter the element to be pushed: ")
        self.stk.insert(0,ele)
    
    def pop(self):
        if not self.stk:
            print("Stack is empty")
            return
        print(f'Popped element is : {self.stk[0]}')
        del self.stk[0]
    
    def display(self):
        if not self.stk:
            print("Stack is empty")
            return
        print(self.stk)

class Menu:
    def __init__(self):
        pass
    def get_menu(self,stack):
        menu = {
            1:stack.push,
            2:stack.pop,
            3:stack.display,
            4:self.end_of_program
            }
        return menu
        
    def invalid_choice(self):
        print("Invalid choice")

    def end_of_program(self):
        sys.exit("End of program")

    def run_menu(self):
        stack=Stack()
        while True:
            ch=int(input("1.push 2.pop 3.display 4.exit: "))
            menu = self.get_menu(stack)
            menu.get(ch, self.invalid_choice)()
menu = Menu()
menu.run_menu()

