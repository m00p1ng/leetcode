from typing import List

class Solution:
    def dfs(self, i: int, n: int, graph: List[List[int]], state: List[int], result: List[List[int]]):
        if i == n:
            result.append(state)
            return

        for v in graph[i]:
            self.dfs(v, n, graph, [*state, v], result)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        n = len(graph)

        self.dfs(0, n-1, graph, [0], result)

        return result

if __name__ == "__main__":
    solution = Solution()

    testcases = [
        [[1,2],[3],[3],[]],
        [[4,3,1],[3,2,4],[3],[4],[]],
    ]

    for t in testcases:
        print(solution.allPathsSourceTarget(t))
