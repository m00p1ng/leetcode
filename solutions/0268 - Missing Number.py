from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numLen = len(nums)
        result = numLen

        for i in range(numLen):
            result ^= nums[i] ^ i

        return result

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1],
    ]

    for t in testcases:
        print(solution.missingNumber(t))
