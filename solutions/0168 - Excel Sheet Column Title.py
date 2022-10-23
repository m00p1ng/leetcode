class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        base = ord('A')

        while columnNumber:
            columnNumber = columnNumber - 1
            result = chr(base + columnNumber % 26) + result
            columnNumber //= 26

        return result


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        1,
        28,
        701,
    ]

    for t in testcases:
        print(solution.convertToTitle(t))
