class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c_0 = 0
        c_1 = 0
        c_2 = 0
        
        for i in nums:
            if i == 0:
                c_0+=1
            if i == 1:
                c_1+=1
            if i ==2:
                c_2+=1
        for i in range(len(nums)):
            if c_0>0:
                nums[i] = 0
                c_0-=1
                continue
            if c_1>0:
                nums[i] = 1
                c_1-=1
                continue
            if c_2>0:
                nums[i] = 2
                c_2-=1
            