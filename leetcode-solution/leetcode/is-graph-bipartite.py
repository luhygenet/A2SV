class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # -1 = red
        # -
        colors = [-1 for _ in range(len(graph))]

        def dfs(i):
            for neighbor in graph[i]:
                if colors[neighbor] != -1:
                    if colors[i] == colors[neighbor]:
                        return False
                else:
                    if colors[i] == 0:
                        colors[neighbor] = 1
                    else:
                        colors[neighbor] = 0
                    if not dfs(neighbor):
                        return False
            return True


        for j in range(len(colors)):
            if colors[j] == -1:
                colors[j] = 0
                if not dfs(j):
                    return False
        return True

                    
