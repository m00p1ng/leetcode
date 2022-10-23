from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numLen = len(nums)
        for i in range(numLen-1):
            curr = nums[i]

            if curr == 0:
                continue

            found = False
            for j in range(i+1, numLen):
                if curr == nums[j]:
                    nums[j] = 0
                    found = True

            if found:
                nums[i] = 0

        return sum(nums)


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [1,2,3,2],
        [1,1,1,1,1],
        [1,2,3,4,5],
    ]

    for t in testcases:
        print(solution.sumOfUnique(t))
