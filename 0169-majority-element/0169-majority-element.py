from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        for i in nums:
            if count == 0:
                temp = i
                count = 1
            elif temp == i:
                count +=1
            else:
                count-=1
        return temp
            
        