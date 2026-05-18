class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for index, num in enumerate(nums):
            if nums[index] > 0:
                break
            elif index > 0 and nums[index] == nums[index - 1]:
                continue
            low = index + 1
            high = len(nums) - 1
            while low < high:
                summ = nums[index] + nums[low] + nums[high]
                if summ == 0:
                    results.append([nums[index], nums[low],nums[high]])
                    low += 1
                    high -= 1
                    while low < high and  nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and  nums[high] == nums[high + 1]:
                        high -= 1
                elif summ < 0:
                    low += 1
                elif summ > 0:
                    high -= 1
        return results