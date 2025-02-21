import sys
class Node:
    def __init__(self,data=0):
        self.left=None
        self.data=data
        self.right=None
class Bst:
    def __init__(self):
        self.root=None

    def add_node(self):
        data=int(input("Enter data for new node: "))
        node=Node(data)
        if self.root is None:
            self.root = node
            return
        temp1 = self.root
        temp2= None
        while temp1 != None:
            temp2 = temp1
            if data <temp1.data:
                temp1=temp1.left
            else:
                temp1=temp1.right
        if data<temp2.data:
            temp2.left = node
        else:
            temp2.right = node
        return
    
    def delete_node(self):
        data = int(input('Enter data of the node to be delete: '))
        temp1 = self.root
        temp2 = None
        while temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        # If node to be deleted is a leaf node:
        if temp1.left is None and temp1.right is None:
            print(f'Node with data {temp1.data} deleted')
            if temp2.left is temp1:
                temp2.left = None
            else:
                temp2.right = None
        # If node to be deleted has 2 children
        elif temp1.left is not None and temp1.right is not None:
            print(f'Node with data {temp1.data} deleted')
            temp3 = temp1.right.left
            if temp3 is None:
                temp1.right.left = temp1.left
            if temp3 is not None:
                while temp3.left is not None:
                    temp3 = temp3.left
                temp3.left = temp1.left
            # if root is the node being deleted
            if temp1 is self.root:
                self.root = temp1.right
                return
            if temp2.left is temp1:
                temp2.left = temp1.right
            else:
                temp2.right = temp1.right
        # when node to be deleted has exactly one child
        else: 
            print(f'Node with data {temp1.data} deleted')
            #link = return () if temp1.left temp1.left else temp1.right
            if temp1 == self.root:
                if temp1.right is None:
                    self.root=temp1.left
                else:
                    self.root=temp1.right
                return
            link = temp1.left # assume temp1 has left child
            if temp1.right:
                link = temp1.right
            if temp2.left is temp1:
                temp2.left = link
            else:
                temp2.right = link


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
        return
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
        return

    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")
        return
    
    def search_node(self):
        if self.root is None:
            print("Tree is empty")
            return
        data=int(input("Enter data to be searched: "))
        temp=self.root
        level=1
        while temp!= None:
            if temp.data==data:
                print(data,"found at level:",level)
                return 
            if data<temp.data:
                temp=temp.left
            else:
                temp=temp.right
            level+=1
        print(data,"is not found")

class Menu:
    def __init__(self):
        pass

    def invalid_choice(self):
        print("Invalid choice")

    def end_of_program(self):
        sys.exit("End of program")

    def user_ch(self,ch,bst):
        match ch:
            case 1:
                bst.add_node()
            case 2 : 
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.delete_node()
            case 3 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.inorder(bst.root)
            case 4 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.preorder(bst.root)
            case 5 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.postorder(bst.root)
            case 6 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.search_node()
            case 7 :
                self.end_of_program()
            case _ :
                self.invalid_choice()                    

    def run_menu(self):
        bst=Bst()
        while True:
            ch=int(input("\n1.add 2.delete 3.inorder 4.preorder 5.postorder 6.search 7.exit: "))
            self.user_ch(ch,bst)
            
menu = Menu()
menu.run_menu()


    
