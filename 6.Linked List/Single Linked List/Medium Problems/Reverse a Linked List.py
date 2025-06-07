class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    

#Driver COde
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    curr=llist.head
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.next
    print()
    llist.reverse()
    while llist.head is not None:
        print(llist.head.data,end=" ")
        llist.head = llist.head.next
