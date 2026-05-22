class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for index, num in enumerate(nums):
            list_to_check = []
            list_to_check = [nums[x] for x in range(len(nums)) if x != index]
            result = 1
            for x in list_to_check: result *= x
            results.append(result)
        return results