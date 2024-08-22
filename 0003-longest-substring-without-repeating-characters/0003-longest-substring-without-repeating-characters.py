class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in strset:
                strset.remove(s[l])
                l+=1
            strset.add(s[r])
            res = max(res,r-l+1)
        return res
        