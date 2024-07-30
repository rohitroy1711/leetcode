class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(lis)->int:
            rob1 = 0
            rob2 = 0
            for i in lis:
                temp = max(i+rob1,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(nums[0],helper(nums[:len(nums)-1]),helper(nums[1:len(nums)]))
                
                
            
        