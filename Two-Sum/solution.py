from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        for ele in nums_dict:
            dif = target-ele
            if dif in nums_dict:
                if ele == dif:
                    if len(nums_dict[ele]) >=2:
                        return nums_dict[ele][:2]
                else:
                    return [nums_dict[ele][0], nums_dict[dif][0]]
