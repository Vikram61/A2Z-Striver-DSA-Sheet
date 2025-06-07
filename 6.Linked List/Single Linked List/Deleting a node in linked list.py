
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None
    
    def delete_node(self,key):
        temp=self.head

        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None

        while temp and temp.data!=key:
            prev=temp
            temp=temp.next

        if not temp:
            return
        prev.next=temp.next
        temp=None
    
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print()

#Driver Code
if __name__ == "__main__":
    list1=LinkedList()
    list1.head=Node(1)
    second=Node(2)
    third=Node(3)
    list1.head.next=second
    second.next=third
    list1.print_list()
    list1.delete_node(2)
    list1.print_list()
    print(list1.search(3))