class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dis = (x**2)+(y**2)
            minHeap.append([dis,x,y])
        heapq.heapify(minHeap)
        res = []
        while k>0:
            m = heapq.heappop(minHeap)
            res.append([m[1],m[2]])
            k = k-1
        return res