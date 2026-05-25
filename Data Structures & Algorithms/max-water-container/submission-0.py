class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        max_container = 0
        container_size = 0
        for index, item in enumerate(heights):
            right = len(heights) - 1
            while index < right:
                container_size = min(heights[index], heights[right]) * (right - index)
                max_container = max(max_container, container_size)
                right -= 1
        return max_container


