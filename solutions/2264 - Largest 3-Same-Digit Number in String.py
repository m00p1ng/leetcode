class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                result = max(result, num[i])

        return result*3

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        "6777133339",
        "2300019",
        "42352338",
    ]

    for t in testcases:
        print(solution.largestGoodInteger(t))
