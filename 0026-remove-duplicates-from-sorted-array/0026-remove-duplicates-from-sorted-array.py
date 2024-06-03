class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 0
        count =0
        for rp in range(1,len(nums)):
            if nums[lp]!=nums[rp]:
                lp+=1
                nums[lp] = nums[rp]
                count+=1
        return count+1
        
        