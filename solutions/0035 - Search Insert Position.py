from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1

        while(l <= h):
            m = (l+h)>>1
            if target == nums[m]:
                return m

            if target > nums[m]:
                l = m + 1
            else:
                h = m - 1

        return l


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        ([1,3,5,6], 5),
        ([1,3,5,6], 2),
        ([1,3,5,6], 7),
        ([1], 1),
    ]

    for t in testcases:
        print(solution.searchInsert(t[0], t[1]))
