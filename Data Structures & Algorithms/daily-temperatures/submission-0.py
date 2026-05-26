class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for left, temp in enumerate(temperatures):
            right = left + 1
            count = 1
            while right < len(temperatures) and temperatures[right] <= temp:
                count += 1
                right += 1  

            if right ==len(temperatures):
                result.append(0)
            else:
                result.append(count)
        return result