class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def res(piles,h,mid)->bool:
            hours = 0
            for i in piles:
                hours+= math.ceil(i/mid)
            if hours<=h:
                return True
            else:
                return False
        
    
        l = 1
        r = max(piles)
        ans = 0
        while l<=r:
            mid = l+(r-l)//2
            if res(piles,h,mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans  
        