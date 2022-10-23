from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        digits = [1] + digits

        return digits


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [1,2,3],
        [4,3,2,1],
        [9],
        [9, 9, 9],
    ]

    for t in testcases:
        print(solution.plusOne(t))
