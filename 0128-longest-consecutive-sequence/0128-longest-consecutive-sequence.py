class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in numset:
                l = 0
                while i+l in numset:
                    l=l+1
                ans = max(ans,l)
        return ans
                    
        