from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count1 = 0
        count2 = 0
        ele1,ele2 = float('-inf'),float('-inf')
        for i in nums:
            if count1 == 0  and i != ele2:
                count1 = 1
                ele1 = i
            elif count2 == 0 and i!=ele1:
                count2 = 1
                ele2 = i
            elif i == ele1:
                count1+=1
            elif i == ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        ct1 = 0
        ct2 = 0
        for i in nums:
            if i == ele1:
                ct1+=1
            if i == ele2:
                ct2+=1
        mini = len(nums)//3
        ans = []
        if ct1>mini:
            ans.append(ele1)
        if ct2>mini:
            ans.append(ele2)
        ans.sort()
        return ans
#         The below is one of the brute force approach
        # elementsCounts = Counter(nums)
        # ans = []
        # for i in elementsCounts:
        #     if elementsCounts[i] > len(nums)//3:
        #         ans.append(i)
        # return ans
        
#         The Below is the optimal approach
            
            