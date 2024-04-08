class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqhash = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preqhash[crs].append(pre)
        output = []
        cycle = set()
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for i in preqhash[crs]:
                if dfs(i) == False:
                    return False
            visit.add(crs)
            output.append(crs)
            cycle.remove(crs)
        
        for i in preqhash:
            if dfs(i) == False:
                return []
        return output
            