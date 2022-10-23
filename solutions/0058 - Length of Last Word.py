class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()

        return len(result[-1])

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
    ]

    for t in testcases:
        print(solution.lengthOfLastWord(t))
