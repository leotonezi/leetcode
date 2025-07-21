from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next
    def __repr__(self):          # handy for quick debugging prints
        return f"{self.val}->{self.next}"

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy node simplifies edge-case handling (empty lists, first pick, etc.)
        dummy = ListNode()       # head sentinel (value doesn’t matter)
        current = dummy          # tail of the merged list we’re building

        while list1 and list2:   # compare current nodes, not their .next
            if list1.val < list2.val:
                current.next = list1   # link the smaller node
                list1 = list1.next     # advance that list
            else:
                current.next = list2
                list2 = list2.next
            current = current.next     # advance the tail

        # Exactly one of list1 / list2 is non-empty; append it wholesale
        current.next = list1 if list1 else list2

        return dummy.next              # skip the sentinel
