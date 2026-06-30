class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        currWtr = 0
        maxWtr = 0

        while l<r:
            if l < r and heights[l] < heights[r]:
                currWtr = abs(r-l) * (heights[l])
                l += 1

            else:
                currWtr = abs(r-l) * (heights[r])
                r -= 1

            maxWtr = max(maxWtr, currWtr)

        return maxWtr
            
