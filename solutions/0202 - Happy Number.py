class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}

        while True:
            if n in visited:
                return False
            visited[n] = True
            sum = self.digitSum(n)

            if sum == 1:
                return True

            n = sum

    def digitSum(self, n: int) -> int:
        sum = 0
        while n:
            remainder = n % 10
            sum += remainder * remainder
            n //= 10

        return sum


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        19,
        2,
    ]

    for t in testcases:
        print(solution.isHappy(t))
