class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {i:[] for i in range(len(nums)+1)}
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i]+=1



        for i,j in hashmap.items():
            countmap[j].append(i)
        
        ans =[]
        for i,j in reversed(countmap.items()):
            while len(j) > 0:
                ans.append(j.pop())
                k = k-1
            if k==0:
                break
        return ans