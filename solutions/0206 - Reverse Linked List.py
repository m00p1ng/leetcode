from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node: Optional[ListNode] = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node

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
        generateListNode([1,2,3,4,5]),
        generateListNode([1,2]),
        generateListNode([]),
    ]

    for t in testcases:
        printListNode(solution.reverseList(t))
