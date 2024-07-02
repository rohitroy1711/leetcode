class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums)
        i = len(nums)-k
        
        heapq.heapify(nums)
        
        while i>0:
            heapq.heappop(nums)
            i=i-1
        return nums[0]        
        
        