# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None :
            return False
        visited = defaultdict(bool)
        currNode = head
        while currNode != None:
            if visited[currNode] :
                return True
            visited[currNode]=True
            currNode =currNode.next
        return False