import sys
class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.ll1=None
    def add_node(self):
        data=int(input("Enter a number: "))
        node=Node(data)
        pos=int(input("Enter the position for addition: "))
        if self.ll1 is None:
            if pos!=1:
                print("Cannot add at given pos: ")
                return
            self.ll1=node
            return
        pre=None
        temp=self.ll1
        if pos==1:
            node.next=temp
            self.ll1=node
            return
        i=1
        while i<pos:
            pre=temp
            temp=temp.next
            i+=1
        if i!=pos:
            print("Node cannot be added at pos:",pos)
            return
        pre.next=node
        node.next=temp
        return 
    def del_node(self):
        pos=int(input("Enter the pos u want to delete: "))
        if pos == 1:
            print(self.ll1.data,"has been deleted")
            self.ll1=self.ll1.next
            return
        i=1
        temp=self.ll1
        pre=None
        while i<pos:
            if temp:
                pre=temp
                temp=temp.next
                i+=1
            else:
                print("There is nothing to delete at pos:",pos)
                return
        if temp:
            print(temp.data,"has been deleted")
            pre.next=temp.next
            return
        else:
            print("There is nothing to delete at pos:",pos)
            return
    def display_rev(self,temp):
        if temp is not None:
            self.display_rev(temp.next)
            print(temp.data,end=" ")
class Menu:
    def __init__(self):
        pass

    def invalid_choice(self):
        print("Invalid choice")

    def end_of_program(self):
        sys.exit("End of program")

    def user_ch(self,ch,ll):
        match ch:
            case 1:
                ll.add_node()
            case 2 : 
                if ll.ll1 is None:
                    print('linked list  is empty')
                else:
                    ll.del_node()
            case 3 :
                if ll.ll1 is None:
                    print('linked list is empty')
                else:
                    ll.display_rev(ll.ll1)
            case 4:
                self.end_of_program()
            case _ :
                self.invalid_choice()                    

    def run_menu(self):
        ll=Linked_list()
        while True:
            ch=int(input("\n1.add 2.delete 3. display 4.exit: "))
            self.user_ch(ch,ll)
            
menu = Menu()
menu.run_menu()


