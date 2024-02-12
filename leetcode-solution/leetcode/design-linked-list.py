class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        idx = 0
        curr = self.head.next
        while curr and idx < index:
            curr = curr.next
            idx += 1
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        temp = self.head.next
        self.head.next = node
        node.next = temp

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        idx = 0
        curr = self.head
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if not curr:
            return  
        temp = curr.next
        curr.next = node
        node.next = temp

    def deleteAtIndex(self, index: int) -> None:
        idx = 0
        curr = self.head
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if not curr or not curr.next:
           return 
        curr.next = curr.next.next
        

      



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)