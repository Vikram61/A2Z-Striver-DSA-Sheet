class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def oddEvenList(self):
        if not self.head or not self.head.next:
            return self.head
        
        odd = self.head
        even = self.head.next
        even_head = even  # Save even list self.head
        
        while even and even.next:
            # Link odd nodes
            odd.next = even.next
            odd = odd.next
            
            # Link even nodes
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return self.head

#Driver Code
if __name__ == "__main__":
    llist=LinkedList()
    llist.head=Node(10)
    llist.head.next=Node(20)
    llist.head.next.next=Node(3)
    llist.head.next.next.next=Node(4)
    llist.head.next.next.next.next=Node(5)

    print("Original Linked List:")
    current = llist.head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

    llist.oddEvenList()
    print("Modified Linked List:")
    current = llist.head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")