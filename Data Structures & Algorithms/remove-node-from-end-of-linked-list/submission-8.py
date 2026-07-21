# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#get the length l of the linkedlist
#the element to delete from the front is the l-n th


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None :
            return None
        slow,fast=head,head
        for _ in range(n):
            fast=fast.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next

        if fast is None:
            head = head.next
        else:
            slow.next = slow.next.next
        return head
        
        
        





















