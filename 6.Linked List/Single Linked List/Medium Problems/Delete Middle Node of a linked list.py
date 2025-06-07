class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node=data
        if self.head==None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def delete_middle(self):

        if self.head is None or self.head.next is None:
            return None
        
        fast=self.head
        slow=self.head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        slow=None
        return self.head

#Driver Code
if __name__ == '__main__':
    llist=LinkedList()
    llist.insert_at_end(Node(1))
    llist.insert_at_end(Node(2))
    llist.insert_at_end(Node(3))
    llist.insert_at_end(Node(4))
    llist.insert_at_end(Node(5))
    print("Original Linked List:")
    curr=llist.head
    while curr:
        print(curr.data, end="->")
        curr=curr.next
    print("None")
    llist.delete_middle()
    print("Modified Linked List:")
    curr=llist.head
    while curr:
        print(curr.data, end="->")
        curr=curr.next
    print("None")   