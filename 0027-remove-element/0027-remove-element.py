class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        c = len(nums)-1
        for r in nums:
            if r !=val:
                nums[l]=r
                l+=1
        return l
                    
    