from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        hashmap = Counter(nums)
        # print(hashmap)
        
        threshold = len(nums)//2
        # print(threshold)
        ans = 0
        for i in hashmap:
            if hashmap[i] > threshold and hashmap[i] > ans:
                ans = i
            
            # print(ans,hashmap[i])
        return ans
            
        