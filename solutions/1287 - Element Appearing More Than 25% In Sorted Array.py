from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        numLen = len(arr)

        i = 0
        while i < numLen:
            cnt = 1
            curr = arr[i]

            i += 1
            while i != numLen and arr[i] == curr:
                cnt += 1
                i += 1

            if cnt > numLen / 4:
                return curr

        return -1

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [1,2,2,6,6,6,6,7,10],
        [1,1],
        [1],
        [1,2,3,3],
        [1,2,3,4,5,6,7,8,9,10,11,12,12,12,12],
    ]

    for t in testcases:
        print(solution.findSpecialInteger(t))
