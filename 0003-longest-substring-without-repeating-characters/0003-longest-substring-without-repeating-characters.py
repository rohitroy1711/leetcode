class Solution(object):
    def lengthOfLongestSubstring(self, s):
        arr = list(s)
        aset = set()
        l = 0
        r = 0
        length = 0
        while r<len(arr):
            if arr[r] not in aset:
                aset.add(arr[r])
                length = max((r-l+1),length)
                r+=1
                
            else:
                while arr[r] in aset:
                    aset.remove(arr[l])
                    l+=1
                aset.add(arr[r])
                length = max((r-l+1),length)
                r+=1
        return length
                
        
        