class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # -1 white
        # 0 grey
        # 1 black
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])

        colors = [-1 for i in range(numCourses)]
        def dfs(j):

            for neighbor in graph[j]:
                if neighbor in graph and colors[neighbor] != -1 and colors[neighbor] != 1:
                    if colors[neighbor] == 0:
                        return True
                if colors[neighbor] == 1:
                    continue

                colors[neighbor] = 0
                if dfs(neighbor):
                    return True
            colors[j] = 1
                
        for i in range(len(colors)):
            if colors[i] == -1 and i in graph:
                colors[i] = 0
                if dfs(i):
                    return False

        return True        

        
         

