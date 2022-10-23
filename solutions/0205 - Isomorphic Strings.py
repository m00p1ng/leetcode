from typing import Dict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(f'{self.genResult(s)=}, {self.genResult(t)=}')
        return self.genResult(s) == self.genResult(t)

    def genResult(self, s: str) -> str:
        d: Dict[str, int] = {}
        cnt = 0
        r: str = ""

        for c in s:
            if c not in d:
                d[c] = cnt
                cnt += 1
            r += f'{d[c]:02d}'

        return r


if __name__ == "__main__":
    solution = Solution()

    testcases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"),
    ]

    for t in testcases:
        print(solution.isIsomorphic(*t))
