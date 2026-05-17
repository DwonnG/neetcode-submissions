class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        items = set()
        remove = []
        for num in nums:
            if num in items:
                remove.append(num)
            items.add(num)
        for item in remove:
            nums.remove(item)
        # print(nums)
        return len(nums)