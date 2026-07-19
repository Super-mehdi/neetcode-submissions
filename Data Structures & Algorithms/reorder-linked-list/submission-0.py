# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#2,4,6,8,10
#2,10,4,8,6
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
    size = length(head)
    currNode = head
    for _ in range(size//2):
        currNode=currNode.next
    secondHalf = currNode.next
    currNode.next = None
    return head,secondHalf
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1,head2=divide(head)
        head2=reversed(head2)
        while head2 != None and head1.next != None:
            tmp1 = head1.next
            tmp2 = head2
            head2=head2.next
            head1.next = tmp2
            tmp2.next = tmp1
            head1=head1.next.next
        









