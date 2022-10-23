class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        1,
        16,
        3,
        8,
        0,
    ]

    for t in testcases:
        print(solution.isPowerOfTwo(t))
