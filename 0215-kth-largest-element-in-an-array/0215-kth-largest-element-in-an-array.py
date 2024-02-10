class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = 0
        e = len(nums)
        n = self.mergesortHelper(nums,s,e)
        return n[e-k]
    def mergesortHelper(self,arr:List[int],s,e)->List[int]:
        if e-s+1 <= 1:
            return arr
        m = s+(e-s)//2
        self.mergesortHelper(arr,s,m)
        self.mergesortHelper(arr,m+1,e)
        
        self.merge(arr,s,m,e)
        return arr
        
    def merge(self,arr:List[int],s,m,e)->None:
        l = arr[s:m+1]
        r = arr[m+1:e+1]
        
        i = 0
        j = 0
        k = s
        
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while  j<len(r):
            arr[k] = r[j]
            j+=1
            k+=1
        