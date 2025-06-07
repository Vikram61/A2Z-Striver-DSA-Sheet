
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def find_length(self):
        count=0

        if not self.head:
            return count
        
        curr=self.head
        while curr:
            count+=1
            curr=curr.next
        return count
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        print()

#Driver Code

if __name__== "__main__":
    llist=LinkedList()
    llist.head=Node(10)
    second=Node(20)
    third=Node(30)
    fourth=Node(40)
    llist.head.next=second
    second.next=third
    third.next=fourth
    llist.print_list()
    print(llist.find_length())
