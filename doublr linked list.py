class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None



    def insert_begin(self,data):
        new_node=Node(data)


        if self.head is not None:
            self.head.prev=new_node
            new_node.next=self.head

        self.head=new_node
        print("Inserted at beginning")


    def insert_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        new_node.prev=temp

        print("Inserted at end")


    def delete_begin(self):
        if self.head is None:
            print("list is empty")
            return

        if self.head is not None:
            self.head.prev=None

        print("deleted from beginning")


    def delete_end(self):
        if self.head is not None:
            print("List is empty")
            return

        temp=self.head
        if temp.next is None:
            self.head=None
            print("deleted last node")
            return

        while temp.next is not None:
            temp=temp.next

        temp.prev.next=None
        print("Deleted from end")


    def display_forward(self):
         if self.head is None:
             print("List is empty")
             return

         temp=self.head
         print("Forward Traversal:")
         while temp is not None:
             print(temp.data,end="<->")
             temp=temp.next
         print("None")


    def display_backward(self):
         if self.head is None:
             print("List is empty")
             return

         temp=self.head
         while temp.next is not None:
             temp=temp.next
         print("Backward Traversal:")
         while temp is not None:
             print(temp.data,end="<->")
             temp=temp.prev
         print("None")



dll=DoublyLinkedList()

while True:

    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display Forward")
    print("6. Display Backward")
    print("7. Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        val=int(input("Enter value:"))
        dll.insert_begin(val)

    if choice==2:
        val=int(input("Enter value:"))
        dll.insert_end(val)    

    elif choice==3:
        dll.delete_begin()

    elif choice==4:
        dll.delete_end()

    elif choice==5:
        dll.display_forward()

    elif choice==6:
        dll.display_backward()

    elif choice==7:
        print("Program Ended")
        break
    else:
        print("Invalid option")


         


         
         


  

             
         
         


        

