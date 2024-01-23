class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y = 0
        d = x
        while d:
            temp = d%10
            y = y*10+temp
            d = d//10
            
        if y == x:
            return True
        else:
            return False
            
        