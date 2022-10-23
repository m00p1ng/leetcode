class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        i = 0
        allowChars = "0123456789"
        sign = 1
        num = 0
        sLen = len(s)

        if i == sLen:
            return 0

        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1

        if i == sLen or s[i] not in allowChars:
            return 0

        while i != sLen and s[i] in allowChars:
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num = sign * num

        MIN = -(1 << 31)
        MAX = (1 << 31) - 1

        if num < MIN:
            return MIN
        if num > MAX:
            return MAX

        return num


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "42",
        "mooping 20",
        "20 mooping",
        " 2    0",
        " - 2",
        "-2mooping",
        "+-12",
        "+12",
        "-+12",
        "   ",
        "+",
    ]

    for t in testcases:
        print(solution.myAtoi(t))
