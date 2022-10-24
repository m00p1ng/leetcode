from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        maxCount = 0
        minNum = 1 << 31

        for n in nums:
            if n & 1:
                continue

            if n not in d:
                d[n] = 0
            d[n] += 1

            if d[n] == maxCount:
                minNum = min(minNum, n)
            elif d[n] > maxCount:
                minNum = n
                maxCount += 1

        if maxCount == 0:
            return -1


        return minNum


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [0,1,2,2,4,4,1],
        [4,4,4,9,2,4],
        [29,47,21,41,13,37,25,7],
        [0,0,0,0],
        [0,1,2,2,4,4,1]
    ]

    for t in testcases:
        print(solution.mostFrequentEven(t))
