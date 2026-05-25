class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequency_dict = {}
        left = 0
        for item in s1:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1

        frequency_dict_s2 = {}
        for right, char in enumerate(s2):
            frequency_dict_s2[char] = frequency_dict_s2.get(char, 0) + 1
            if right - left + 1 > len(s1):
                left_char = s2[left]
                frequency_dict_s2[left_char] -= 1
                
                if frequency_dict_s2[left_char] == 0:
                    del frequency_dict_s2[left_char]

                left += 1
            if frequency_dict_s2 == frequency_dict:
                return True
        return False