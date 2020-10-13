class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        if not nums1:
            mid = (len(nums2)-1) // 2
            if len(nums2)%2 == 1:
                return nums2[mid]
            else:
                return ((nums2[mid] + nums2[mid+1]) * 1.0) / 2
        
        INT_MAX = 10**9 + 7
        INT_MIN = -1 * INT_MAX
        
        l1 = len(nums1)
        l2 = len(nums2)
        total = l1+l2
        half = total // 2
        if total % 2 == 1:
            half += 1
        
        i,j = 0,l1-1
        while True:
            mid = i + (j-i)//2
            
            ul = INT_MIN if mid < 0 else nums1[mid]
            ur = INT_MAX if (mid+1) >= l1 else nums1[mid+1]
            
            lpos = half - (mid + 1) - 1
            ll = INT_MIN if lpos < 0 else nums2[lpos]
            lr = INT_MAX if (lpos+1) >= l2 else nums2[lpos+1]
            
            if ul <= lr and ll <= ur:
                if total%2 == 0:
                    return ((max(ul,ll) + min(ur,lr)) * 1.0) / 2
                else:
                    return min(max(ul,ll),min(ur,lr))
            
            if ul > lr:
                j = mid-1
                continue
            if ll > ur:
                i = mid+1
                continue
        return INT_MIN
