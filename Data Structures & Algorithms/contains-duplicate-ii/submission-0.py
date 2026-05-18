class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # lp = 0
        # rp = 1
        seen = {}
        for index, num in enumerate(nums):
            # lp = 0
            # rp = 1
            # while lp < rp:
            #     if nums[lp] == nums[rp] and abs(lp - rp) <= k:
            #         return True
            #     seen[num]
            if num in seen and abs(seen[num] - index) <= k:
                return True
            seen[num] = index
        return False
                