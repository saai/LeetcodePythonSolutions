class Solution:
	def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(0,numCourses)]
        visit = [0 for _ in range(0, numCourses)]
        for prr in prerequisites:
            graph[prr[0]].append(prr[1])
            
        def dfs(i):
            if visit[i]==-1:
                return False
            elif visit[i]==1:
                return True
            visit[i]=-1
            for j in graph[i]:
                if dfs(j)== False:
                    return False
            visit[i]=1
            return True
        for i in range(0,numCourses):
            if dfs(i)==False:
                return False
        return True
    