class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWtr = 0
        currWtr = 0
        while l< r:
            if heights[l]< heights[r]:
                currWtr = (r-l) * abs(heights[l])
                l += 1
            else:
                currWtr = (r-l) * abs(heights[r])
                r -= 1

            maxWtr = max(currWtr, maxWtr)
        return maxWtr
