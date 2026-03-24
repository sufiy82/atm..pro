#node class represents each element of the linked list
class node:

    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        print("Node inserted at beginning")


    def insert_end(self_data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print("Node inserted as first node")  
            return
        temp=self.head
        
        while temp.next:
            temp=temp.next
        temp.next=new_node
        print("Node inserted at end")
        

    def delete(self,key):
        temp=self.head

        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            print("Node deleted")
            return
        prev=None

        while temp and temp.data!=key:
            
            
        
