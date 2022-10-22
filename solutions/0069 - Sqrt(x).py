class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, 65536):
            if x < i*i:
                return i-1

        return -1

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        4,
        8,
        127,
        256,
        9,
    ]

    for t in testcases:
        print(solution.mySqrt(t))
