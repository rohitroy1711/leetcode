class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSortHelper(nums,0,len(nums)-1)
    def mergeSortHelper(self,nums:List[int],s,e)->List[int]:
        if e-s+1 <=1:
            return nums
        m = s+(e-s)//2
        self.mergeSortHelper(nums,s,m)
        self.mergeSortHelper(nums,m+1,e)
        
        self.merge(nums,s,m,e)
        return nums
    def merge(self,arr:List[int],s,m,e)->None:
        l = arr[s:m+1]
        r = arr[m+1:e+1]
        i = 0
        j = 0
        k = s
        
        while i < len(l) and j < len(r):
            if l[i]<=r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k] = r[j]
            j+=1
            k+=1
        