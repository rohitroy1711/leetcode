class Solution(object):
    def reversePairs(self, nums):
        self.fans = 0
        
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left,right)
        
        def merge(left,right):
            j=0
            for i in left:
                while j < len(right) and i > 2*right[j]:
                        j+=1
                self.fans += j
            sorted_arr = []
            i=0
            j=0
            while i<len(left) and j<len(right):
                
                if left[i]<right[j]:
                    sorted_arr.append(left[i])
                    i+=1
                else:
                    sorted_arr.append(right[j])
                    j+=1
            while i<len(left):
                sorted_arr.append(left[i])
                i+=1
            while j<len(right):
                sorted_arr.append(right[j])
                j+=1
            return sorted_arr
        merge_sort(nums)
        return self.fans
                
       
                
            
        
    
#         This question can be done with the help of merge sort 
#          We start breaking the list with the help of merge sort and then when we are sorting them back we will check for these conditions and then if these conditions saisfy then we will add then to the answer
#         The above method is the optimal way to solve this problem
        
        
        
#         count = 0
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if i>=0 and i<j and j<len(nums):
#                     if nums[i] > 2*nums[j]:
#                         count+=1
#         return count
                
#         Brute force technique
        