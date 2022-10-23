# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 75

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        h = n

        while h - l != 1:
            m = (l+h) >> 1

            if isBadVersion(m):
                h = m
            else:
                l = m

        return h

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        200,
    ]

    for t in testcases:
        print(solution.firstBadVersion(t))
