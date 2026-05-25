class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_container = 0
        
        while left < right:
            container_size = min(heights[left], heights[right]) * (right - left)
            max_container = max(max_container, container_size)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_container


