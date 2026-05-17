class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                return num
            else:
                seen[num] = 1
                # print(seen.get(num, 0))
                # seen[num] = seen.get(num, 0) += 1