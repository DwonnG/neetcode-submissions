from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            anagram = "".join(sorted(s))
            answer[anagram].append(s)
        return list(answer.values())