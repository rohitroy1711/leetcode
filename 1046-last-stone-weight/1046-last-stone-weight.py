import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums  = stones
        while len(nums) > 1:
            heapq._heapify_max(nums)
            num1 = (heapq.heappop(nums))
            heapq._heapify_max(nums)
            num2 = heapq.heappop(nums)
            num3 = abs(num1-num2)
            heapq.heappush(nums,num3)
        if len(nums) == 0:
            return 0
        else:
            return nums[0]