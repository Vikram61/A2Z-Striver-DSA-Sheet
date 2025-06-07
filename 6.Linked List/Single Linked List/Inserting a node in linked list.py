

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data)

        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        current=self.head
        while current.next:
            current=current.next
        
        current.next=node
    
    def insert_after_a_node(self,prev,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        current=self.head
        while current and current.data!=prev:
            current=current.next
        if not current:
            print(f"The node is not present")
            return
        node.next=current.next
        current.next=node

#Driver Code

if __name__ == "__main__":

    list1=LinkedList()
    list1.insert_at_beginning(1)
    list1.insert_at_beginning(2)
    list1.insert_at_end(4)
    list1.insert_at_end(3)
    list1.insert_after_a_node(2,5)
    list1.insert_at_beginning(9)
    current=list1.head
    while current:
        print(current.data,end=" ")
        current=current.next
    print()