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
        if self.ll1 is None:
            self.ll1=node
            return
        temp=self.ll1
        while temp.next is not None:
            temp=temp.next
        temp.next=node
    def add_ll2(self,ob2):
        temp=self.ll1
        while temp.next is not None:
            temp=temp.next
        temp.next=ob2.ll1
    def converge(self,ob2):
        temp1 = self.ll1
        while temp1 is not None:
            temp2=ob2.ll1
            while temp2 is not None:
                if temp1 is temp2:
                    print("\nConverging at",temp1.data)
                    return
                temp2=temp2.next
            temp1=temp1.next
        print("Not converging")
    def display(self,temp):
        if temp is not None:
            print(temp.data,end=" ")
            self.display(temp.next)
            

l1=Linked_list()
n1=int(input("Enter the no of elements in list 1: "))
for i in range(n1):
    l1.add_node()
l2=Linked_list()
n2=int(input("Enter the no of elements in list 2: "))
for i in range(n2):
    l2.add_node()
print("list 1")
l1.display(l1.ll1)
print("\nlist 2")
l2.display(l2.ll1)
l1.add_ll2(l2)
print("\nlist 1")
l1.display(l1.ll1)
l1.converge(l2)
