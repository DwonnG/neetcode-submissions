class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen_2 = {}

        for item in s:
            seen[item] = seen.get(item, 0) + 1

        for item in t:
            seen_2[item] = seen_2.get(item, 0) + 1

        return seen == seen_2
