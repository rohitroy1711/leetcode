class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tot = m+n
        for i in range(tot):
            if i>m-1:
                nums1[i]=nums2[i-m]
        nums1.sort()