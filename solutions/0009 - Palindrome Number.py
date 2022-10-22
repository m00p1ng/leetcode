from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revX = 0
        temp = x

        while temp > 0:
            revX = (revX * 10) + (temp % 10)
            temp = int(temp / 10)

        return x == revX


if __name__ == "__main__":
    solution = Solution()

    testcases: List[int] = [
        121,
        -121,
        10,
    ]

    for t in testcases:
        print(solution.isPalindrome(t))
