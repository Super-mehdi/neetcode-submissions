# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#get the length l of the linkedlist
#the element to delete from the front is the l-n th

def getLength(head):
    length = 0
    while head is not None:
        length +=1
        head = head.next
    return length
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode = head 
        length = getLength(head)

        if length == 1 :
            return None
        
        if length == n:
            head = head.next
            return head
        
        for _ in range(length-n-1):
            currNode = currNode.next
        
        if currNode is not None and currNode.next is not None:
            currNode.next = currNode.next.next
        else:
            currNode.next=None
        
        return head
        
        





















