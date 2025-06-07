
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None
    def isPalindrome(self) -> bool:
        if not self.head or not self.head.next:
            return True  # Empty list or 1 node is always a palindrome
        
        # Step 1: Find the middle (slow will point to middle)
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare first half and reversed second half
        first_half = self.head
        second_half = prev
        
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
#Driver Code

if __name__ == "__main__":
    llist=LinkedList()
    llist.head=Node(1)
    llist.head.next=Node(2)
    llist.head.next.next=Node(2)
    llist.head.next.next.next=Node(1)
    print(llist.isPalindrome())
