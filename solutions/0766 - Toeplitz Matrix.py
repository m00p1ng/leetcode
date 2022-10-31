from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [
            [1,2,3,4],
            [5,1,2,3],
            [9,5,1,2],
            [0,9,5,1],
        ],
        [
            [1,2,3,4,5],
            [0,1,2,3,4],
        ],
        [
            [1,2],
            [2,2]
        ],
        [
            [1,0],
            [2,1],
            [3,2],
            [4,3],
            [5,4],
        ],
        [
            [36,59,71,15,26,82,87],
            [56,36,59,71,15,26,82],
            [15, 0,36,59,71,15,26],
        ],
        [
            [41,45],
            [81,41],
            [73,81],
            [47,73],
            [ 0,47],
            [79,76]
        ]
    ]

    for t in testcases:
        print(solution.isToeplitzMatrix(t))
