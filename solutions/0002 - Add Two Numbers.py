from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'[val={self.val},next={self.next}]'

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        carry = 0

        while l1 != None or l2 != None or carry:
            sum = carry

            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            curr.next = ListNode(val=sum%10)
            carry = sum//10
            curr = curr.next

        return result.next

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
        (generateListNode([2,4,3]), generateListNode([5,6,4])),
        (generateListNode([0]), generateListNode([0])),
        (generateListNode([9,9,9,9,9,9,9]), generateListNode([9,9,9,9])),
    ]

    for t in testcases:
        printListNode(solution.addTwoNumbers(*t))
