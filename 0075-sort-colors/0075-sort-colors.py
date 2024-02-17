class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for i in nums:
            colors[i] += 1
        m=0
        for i in range (0,len(colors)):
            for j in range (0,colors[i]):
                nums[m] = i
                m+=1
        