class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        bp = 1
        bl = 1

# we need to run the lop from start to end and end to last

        for i in range(len(nums)):
            if i==0:
                output.append(1)
                continue
            bp = bp*nums[i-1]
            output.append(bp)



        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                continue
            bl = bl*nums[i+1]
            output[i] = output[i]*bl
        return output
    