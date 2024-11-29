from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        elementsCounts = Counter(nums)
        ans = []
        for i in elementsCounts:
            if elementsCounts[i] > len(nums)//3:
                ans.append(i)
        return ans
        