class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = {}
        sLen = len(s)

        for i in range(sLen):
            c = s[i]
            if c not in visited:
                visited[c] = 0
            visited[c] += 1

        for i in range(sLen):
            c = s[i]
            if visited[c] == 1:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "leetcode",
        "loveleetcode",
        "aabb",
    ]

    for t in testcases:
        print(solution.firstUniqChar(t))
