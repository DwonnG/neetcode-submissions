class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation_s1 = "".join(sorted(s1))
        left = 0

        for right in range(len(s2)):
            if right < len(s1) - 1:
                continue
            sub = s2[left:right+1]
            permutation_s2 = "".join(sorted(sub))               
            if permutation_s2 == permutation_s1:
                return True
            else:
                left += 1
        return False