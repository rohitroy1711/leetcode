class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x,y in points:
            dist = (x*x)+(y*y)
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        
        while k>0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k = k-1
            
        return res