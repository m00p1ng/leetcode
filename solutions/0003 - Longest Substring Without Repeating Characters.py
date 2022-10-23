class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        visited = {}
        sLen = len(s)
        i = 0

        while i != sLen:
            if s[i] in visited:
                max_count = max(max_count, count)
                i = visited[s[i]] + 1
                visited = {}
                count = 1
            else:
                count += 1

            visited[s[i]] = i
            i += 1


        return max(max_count, count)


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        'abcabcbb',
        'bbbbb',
        'pwwkew',
        ' ',
        'dvdf',
    ]

    for t in testcases:
        print(solution.lengthOfLongestSubstring(t))
