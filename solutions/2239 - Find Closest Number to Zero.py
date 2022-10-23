from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minDis = 1 << 31
        minNum = -minDis

        for n in nums:
            dis = abs(n)
            if minDis >= dis:
                if minDis == dis:
                    minNum = max(minNum, n)
                else:
                    minNum = n
                minDis = dis

        return minNum


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [-4,-2,1,4,8],
        [2,-1,1],
        [-100000,-100000],
    ]

    for t in testcases:
        print(solution.findClosestNumber(t))
