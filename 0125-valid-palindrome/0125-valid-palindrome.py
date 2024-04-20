class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        n_s = ""
        for i in s:
            if ord(i) >= 97 and ord(i) <123 or ord(i) >=48 and ord(i)<=57:
                n_s = n_s+i
                

        lp=0
        rp = len(n_s)-1

        while rp>lp:
            if n_s[rp] == n_s[lp]:
                rp-=1
                lp+=1
            else:
                return False
                
        return True