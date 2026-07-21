# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(head1, head2):
    currNode1,currNode2=head1,head2
    dummy =res = ListNode(0)
    while currNode1 != None and currNode2 != None:
        if currNode1.val <= currNode2.val :
            res.next = currNode1
            currNode1=currNode1.next
        else:
            res.next = currNode2
            currNode2=currNode2.next
        res = res.next
    res.next = currNode1 if currNode1 else currNode2
    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2 :
            return mergeTwoLists(lists[0],lists[1])
        return mergeTwoLists(self.mergeKLists(lists[:n//2]),self.mergeKLists(lists[n//2:]))





