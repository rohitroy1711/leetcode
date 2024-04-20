class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        curmax = 0
        while l<r:
            area = (min(h[l],h[r]))*((r+1)-(l+1))
            #print(area)
            if h[l]<= h[r]:
                l+=1
                if area>=curmax:
                    curmax = area
            else:
                if area >= curmax:
                    curmax = area
                r-=1
    

        return (curmax)
        
        