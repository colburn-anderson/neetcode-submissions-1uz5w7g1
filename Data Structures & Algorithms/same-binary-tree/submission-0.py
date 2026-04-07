# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pue = deque([p])
        que = deque([q])

        while pue and que:
            
            for _ in range(len(pue)):
                nodeP = pue.popleft()
                nodeQ = que.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                pue.append(nodeP.left)
                pue.append(nodeP.right)
                que.append(nodeQ.left)
                que.append(nodeQ.right)
        return True
