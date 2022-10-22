from typing import List, Tuple

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            val = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == val:
                    return [i, j]

        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()

    testcases: List[Tuple[List[int], int]] = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6)
    ]

    for t in testcases:
        print(solution.twoSum(t[0], t[1]))

