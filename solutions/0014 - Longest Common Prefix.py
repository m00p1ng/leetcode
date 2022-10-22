from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = strs[0]

        for s in strs:
            sLen = len(s)

            if sLen == 0:
                return ""

            for i in range(sLen):
                if i == len(result):
                    break
                if i + 1 == sLen:
                    result = result[:sLen]
                if s[i] != result[i]:
                    result = result[:i]
                    break

        return result

if __name__ == "__main__":
    solution = Solution()

    testcases: List[List[str]] = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["ab", "a"],
        ["abab", "aba", ""],
        ["mooping"],
    ]

    for t in testcases:
        print(solution.longestCommonPrefix(t))
