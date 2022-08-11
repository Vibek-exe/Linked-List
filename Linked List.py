class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
            
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is  None:
            self.head = new_node
            
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = new_node
            
    def add_after(self,data,p):     #p = position after which node we want to insert new node   
            n = self.head
            while n is not None:
                if p == n.data:
                    break
                n = n.ref
            if n is None:
                print("Node is Not Present in the Linked List")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                
                
            
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)

LL1.add_end(80)

#  40 30 20 10 80

LL1.print_LL()
        
LL1.add_after(200,20)

# 40 30 20 200 10 80 

print()

LL1.print_LL()
        
        
        
        
        