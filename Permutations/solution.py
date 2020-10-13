class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
                
        start = list(nums)
        result = [start]
        
        self.nextPermutation(nums)
        while(nums != start):
            result.append(list(nums))
            self.nextPermutation(nums)            
        
        return result
            
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
