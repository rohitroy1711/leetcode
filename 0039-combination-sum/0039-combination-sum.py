class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr =[]
        def dfs(i,curr):
            if sum(curr) > target or i>=len(candidates):
                return
            elif sum(curr) == target:
                result.append(curr.copy())
                return
            curr.append(candidates[i])
            dfs(i,curr)
            curr.pop()
            dfs(i+1,curr)
        dfs(0,curr)
        return result
        