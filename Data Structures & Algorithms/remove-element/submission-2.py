class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count = 0
        # remove = []
        # for index, item in enumerate(nums):
        #     if item == val:
        #         count += 1
        #         remove.append(item)

        
        # for num in remove:
        #     nums.remove(num)

        # return len(nums)

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

        