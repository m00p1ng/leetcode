from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = ""

        while head:
            result += str(head.val)
            head = head.next

        return result == result[::-1]

# Testcases
def generateListNode(list: List[int]) -> Optional[ListNode]:
    root = ListNode()
    curr = root

    for i in list:
        curr.next = ListNode(val=i)
        curr = curr.next

    return root.next

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        generateListNode([1,2,2,1]),
        generateListNode([1,2]),
        generateListNode([1]),
        generateListNode([1,3,0,2]),
        generateListNode([1,0,1]),
        generateListNode([1,0,0]),
    ]

    for t in testcases:
        print(solution.isPalindrome(t))
