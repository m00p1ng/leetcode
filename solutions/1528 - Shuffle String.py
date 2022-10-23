from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sLen = len(s)
        result = list(s)
        for i in range(sLen):
            result[indices[i]] = s[i]

        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        ("codeleet", [4,5,6,7,0,2,1,3]),
        ("abc", [0,1,2]),
    ]

    for t in testcases:
        print(solution.restoreString(*t))
