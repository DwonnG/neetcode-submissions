class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            if nums[lp] == nums[rp] and len(nums) > 1:
                return True
            elif nums[lp] in seen or nums[rp] in seen:
                return True
            else:
                seen.append(nums[lp])
                seen.append(nums[rp])
                lp += 1
                rp -= 1
        return False