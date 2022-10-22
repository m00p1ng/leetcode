from typing import Optional, List, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"[val={self.val},next={self.next}]"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                result.append(list1.val)
                list1 = list1.next
            else:
                result.append(list2.val)
                list2 = list2.next

        while list1 != None:
            result.append(list1.val)
            list1 = list1.next

        while list2 != None:
            result.append(list2.val)
            list2 = list2.next


        return self.generateListNode(result)


    def generateListNode(self, list: List[int]) -> Optional[ListNode]:
        if len(list) == 0:
            return None
        if len(list) == 1:
            return ListNode(val=list[0])

        reversed: List[int] = sorted(list, reverse=True)
        lastNode: ListNode = ListNode(val=reversed[0])
        node: ListNode = ListNode()

        for n in reversed[1:]:
            node = ListNode(n, lastNode)
            lastNode = node

        return node

### Testcases
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

    testcases: List[Tuple[Optional[ListNode], Optional[ListNode]]] = [
        (solution.generateListNode([1,2,4]), solution.generateListNode([1,3,4])),
        (solution.generateListNode([]), solution.generateListNode([0])),
        (solution.generateListNode([1]), solution.generateListNode([])),
    ]

    for t in testcases:
        printListNode(solution.mergeTwoLists(t[0], t[1]))
