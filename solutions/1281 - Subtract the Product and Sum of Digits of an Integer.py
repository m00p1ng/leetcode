class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1

        while n:
            i = n % 10
            sum += i
            mul *= i

            n //= 10

        return mul - sum

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        234,
        4421,
    ]

    for t in testcases:
        print(solution.subtractProductAndSum(t))
