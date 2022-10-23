class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = str(abs(x))[::-1]

        result = sign * int(num)

        if result > (1 << 31) - 1 or result < -(1 << 31):
            return 0

        return result

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        123,
        -123,
        120,
        1534236469,
    ]

    for t in testcases:
        print(solution.reverse(t))
