class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in tracker:
                return [tracker[complement], index]
            tracker[num] = index