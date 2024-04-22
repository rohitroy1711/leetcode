class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        mid = 0
        l = 0
        h = len(nums)-1
        index = -1
        while l<=h:
            mid = l +(h-l)//2
            if target == nums[mid] :
                    #print("h",mid)
                    return mid
            if nums[l] <= nums[mid]:
                    if target >= nums[l] and target < nums[mid]:
                        h=mid
                    else:
                        l = mid+1
            else:
                    if target <= nums[h] and target > nums[mid]:
                        l=mid+1
                    else:
                        h = mid

        return index