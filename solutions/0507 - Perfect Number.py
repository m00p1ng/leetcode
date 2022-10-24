class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        l = int(num ** 0.5)
        sum = 1

        for i in range(2, l + 1):
            if num % i != 0:
                continue

            sum += i + num // i

        return sum == num

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        28,
        7,
        1,
        14,
    ]

    for t in testcases:
        print(solution.checkPerfectNumber(t))
