class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_maps = {}
        for word in strs:
            word_sort = sorted(list(word))
            word_sort =''.join(word_sort)
            if word_sort in words_maps:
                words_maps[word_sort].append(word)
            else:
                words_maps[word_sort] = [word]
        answer = list(words_maps.values())
        return answer
