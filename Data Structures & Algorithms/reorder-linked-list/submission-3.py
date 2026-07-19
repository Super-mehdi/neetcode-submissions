# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def length(head):
    length = 0
    currNode = head
    while currNode != None:
        length+=1
        currNode = currNode.next
    return length
def reversed(head):
    currNode, prev = head, None
    while currNode != None:
        tmp = currNode.next
        currNode.next = prev
        prev= currNode
        currNode = tmp
    return prev

def divide(head):
    firstHalf,secondHalf=head,None
    currNode1,currNode2=head,head.next
    while currNode2 is not None and currNode2.next is not None:
        currNode1=currNode1.next
        currNode2=currNode2.next.next
    secondHalf = currNode1.next
    currNode1.next = None
    return firstHalf,secondHalf
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1,head2=divide(head)
        head2=reversed(head2)
        while head2 is not None:
            tmp1 = head1.next
            tmp2 = head2
            head2=head2.next
            head1.next = tmp2
            tmp2.next = tmp1
            head1=head1.next.next
        









