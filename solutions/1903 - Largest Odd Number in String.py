class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if (ord(num[i]) - ord('0')) & 1:
                return num[:i+1]

        return ""

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "52",
        "4206",
        "35427",
    ]

    for t in testcases:
        print(solution.largestOddNumber(t))
