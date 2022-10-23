from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}

        for n in nums:
            if n in visited:
                return True
            visited[n] = True

        return False

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2],
    ]

    for t in testcases:
        print(solution.containsDuplicate(t))
