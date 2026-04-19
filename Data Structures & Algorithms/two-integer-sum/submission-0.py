class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], index]
            indices[num] = index