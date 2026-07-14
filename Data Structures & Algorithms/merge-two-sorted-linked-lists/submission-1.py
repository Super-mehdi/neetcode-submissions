# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currNode1,currNode2=list1,list2
        if currNode1 == None:
            return currNode2
        if currNode2 == None:
            return currNode1
        res = None
        if currNode1.val <= currNode2.val:
            res = currNode1
            currNode1 = currNode1.next
        else:
            res = currNode2
            currNode2 = currNode2.next
        currRes = res
        while currNode1 != None and currNode2 != None:
            if currNode1.val <= currNode2.val:
                currRes.next=currNode1
                currNode1=currNode1.next
            else :
                currRes.next = currNode2
                currNode2=currNode2.next
            currRes = currRes.next
        if currNode1 != None :
            currRes.next = currNode1
        if currNode2 != None :
            currRes.next = currNode2
        return res

