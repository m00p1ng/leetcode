from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode()
        temp = root
        stack = []

        while head:
            temp.next = head
            temp = temp.next
            stack.append(head)
            head = head.next

        next = None
        curr = None
        for _ in range(n):
            next = curr
            curr = stack.pop()

        if len(stack) == 0:
            root.next = next
        else:
            prev = stack.pop()
            prev.next = next

        return root.next

## Testcases
def generateListNode(list: List[int]) -> Optional[ListNode]:
    root = ListNode()
    curr = root

    for i in list:
        curr.next = ListNode(val=i)
        curr = curr.next

    return root.next

def printListNode(list: Optional[ListNode]):
    node = list

    while node != None:
        print(f'{node.val}', end="")
        node = node.next
        if node != None:
            print("->", end="")
        else:
            print()

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        (generateListNode([1,2,3,4,5]), 2),
        (generateListNode([1]), 1),
        (generateListNode([1, 2]), 1),
    ]

    for t in testcases:
        printListNode(solution.removeNthFromEnd(*t))
