from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0

        for n in nums:
            num ^= n

        return num

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [2,2,1],
        [4,1,2,1,2],
        [1],
    ]

    for t in testcases:
        print(solution.singleNumber(t))
