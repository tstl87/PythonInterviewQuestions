class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        

        from collections import defaultdict
        graph = defaultdict(list)
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        
        path = set()
        
        # True if there is a cycle, False if not
        def visit(vertex):
            path.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor in path or visit(neighbor):
                    return True
            path.remove(vertex)
            return False
        
        for i in range(numCourses):
            if visit(i):
                return False
        return graph
    
    
print( Solution().canFinish(2,[[1,0]]))