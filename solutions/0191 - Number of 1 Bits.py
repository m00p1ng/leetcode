from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0

        while n:
            sum += (n & 1)
            n >>= 1

        return sum


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        0b00000000000000000000000000001011,
        0b00000000000000000000000010000000,
        0b11111111111111111111111111111101,
    ]

    for t in testcases:
        print(solution.hammingWeight(t))
