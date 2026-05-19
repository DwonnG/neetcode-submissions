class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        openings = bracket_map.values()
        for char in s:
            if char in openings:
                stack.append(char)
            elif not stack:
                return False
            elif bracket_map[char] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack

