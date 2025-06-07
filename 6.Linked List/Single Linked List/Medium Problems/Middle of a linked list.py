
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#Driver COde
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=sixth
    
    middle=llist.find_middle()
    
    while middle:
        print(middle.data,end=" ")
        middle=middle.next
    print()