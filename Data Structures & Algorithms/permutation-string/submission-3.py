class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_dict = {}
        left = 0
        for item in s1:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1

        for right in range(len(s2)):
            if right < len(s1) - 1:
                continue
            sub = s2[left:right+1]
            frequency_dict_s2 = {}
            for item in sub:
                frequency_dict_s2[item] = frequency_dict_s2.get(item, 0) + 1

            if frequency_dict_s2 == frequency_dict:
                return True
            else:
                left += 1
        return False