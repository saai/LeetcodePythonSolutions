class Solution:
	def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        order = []
        def dfs(i):
            if visit[i]==-1:
                return None
            if visit[i]==1:
                return order
            visit[i]=-1
            for j in graph[i]:
                r = dfs(j)
                if r == None:
                    return None
            visit[i]=1
            order.append(i)
            return order
        for i in xrange(numCourses):
            r = dfs(i) 
            if r == None:
                return []
        return order
