class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9

        return num % 9


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        38,
        0,
        18,
        27,
    ]

    for t in testcases:
        print(solution.addDigits(t))
