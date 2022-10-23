class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = 0
        for c in word:
            if c.isupper():
                cap += 1

        if cap == 0 or cap == len(word):
            return True

        if cap == 1 and word[0].isupper():
            return True

        return False

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "USA",
        "FlaG",
        "g",
    ]

    for t in testcases:
        print(solution.detectCapitalUse(t))
