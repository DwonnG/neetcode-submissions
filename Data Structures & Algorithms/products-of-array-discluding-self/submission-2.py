class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # results = []
        # for index, num in enumerate(nums):
        #     list_to_check = [nums[x] for x in range(len(nums)) if x != index]
        #     result = 1
        #     for x in list_to_check: result *= x
        #     results.append(result)
        # return results
        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result