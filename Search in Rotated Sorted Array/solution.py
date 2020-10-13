def search(self, nums, target: int) -> int:
    n = len(nums)
    res = self.bSearch(nums,target,0,n-1)
    return res
def bSearch(self,nums,target,start,end):
    if start>end:
        return -1
    mid = (start+end)//2
    if nums[mid]==target:
        return mid
    
    if nums[mid]>=nums[start]:
        if nums[start]<=target and target<=nums[mid]:
            return self.bSearch(nums,target,start,mid-1)
        return self.bSearch(nums,target,mid+1,end)
    else:
        if nums[mid]<=target and target<=nums[end]:
            return self.bSearch(nums,target,mid+1,end)
        return self.bSearch(nums,target,start,mid-1)
