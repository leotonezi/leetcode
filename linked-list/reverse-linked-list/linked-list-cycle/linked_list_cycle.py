# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        curr = head

        while curr != None:  # Check curr, not curr.next
            if curr in visited_nodes:  # Check the node itself, not its value
                return True
            visited_nodes.add(curr)  # Add the node, not its value
            curr = curr.next

        return False
