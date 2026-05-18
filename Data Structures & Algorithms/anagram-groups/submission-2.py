from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_maps = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1  # get index of the char

            key = tuple(count)
            words_maps[key].append(s)
        return list(words_maps.values())




        