class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        seen2 = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        
        for char in t:
            seen2[char] = seen2.get(char, 0) + 1

        return seen == seen2
        