from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr: List[List[int]] = [[]]*numRows

        for i in range(numRows):
            arr[i] = [0]*(i + 1)
            arr[i][0] = 1
            arr[i][i] = 1
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

        return arr

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        1,
        5,
        10,
    ]

    for t in testcases:
        print(solution.generate(t))
