class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        openings = bracket_map.values()
        for item in s:
            if item in openings: 
                stack.append(item)
            elif not stack or bracket_map[item] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack