from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        (["ab", "c"], ["a", "bc"]),
        (["a", "cb"], ["ab", "c"]),
        (["abc", "d", "defg"], ["abcddefg"]),
    ]

    for t in testcases:
        print(solution.arrayStringsAreEqual(*t))

