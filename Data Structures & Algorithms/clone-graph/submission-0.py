"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()
        def dfs(node):
            if not node:
                return
            newNode = Node(val = node.val)
            visited[node]=newNode
            if node.neighbors :
                for neighbor in node.neighbors:
                    if neighbor not in visited and not newNode.neighbors:
                        newNode.neighbors = []
                    neighborClone = dfs(neighbor) if neighbor not in visited else visited[neighbor]
                    newNode.neighbors.append(neighborClone)
            return newNode
        return dfs(node)



