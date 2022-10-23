class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        sLen = len(s)
        result = ""
        base = ord('a') - 1

        while i < sLen:
            if i + 2 < sLen and s[i + 2] == "#":
                result += chr(base + int(s[i:i+2]))
                i += 3
            else:
                result += chr(base + int(s[i]))
                i += 1

        return result

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "10#11#12",
        "1326#",
    ]

    for t in testcases:
        print(solution.freqAlphabets(t))
