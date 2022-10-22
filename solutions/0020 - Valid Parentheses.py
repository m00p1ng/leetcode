from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                p = stack.pop()
                if c == ")" and p != "(":
                    return False
                if c == "]" and p != "[":
                    return False
                if c == "}" and p != "{":
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    testcases: List[str] = [
        "()",
        "()[]{}",
        "(]",
        "(",
        "((",
        "]",
    ]

    for t in testcases:
        print(solution.isValid(t))
