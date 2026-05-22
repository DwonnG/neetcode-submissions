from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))
            answer[word].append(s)

        return list(answer.values())