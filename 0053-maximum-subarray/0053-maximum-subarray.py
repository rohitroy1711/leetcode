import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum = 0
        for i in range(0,len(nums)):
            sum+=nums[i]
            maxi = max(sum,maxi)
            if sum<0:
                sum=0
        return maxi
        