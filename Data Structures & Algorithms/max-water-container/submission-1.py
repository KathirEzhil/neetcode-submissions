class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        # two pointers

        fp = 0
        bp = n-1

        max_amt = 0
        area = 0

        while fp < bp:

            area = (bp-fp)*min(heights[fp],heights[bp])

            if area > max_amt:
                max_amt = area
            
            if heights[fp] <= heights[bp]:
                fp +=1
            elif heights[fp] > heights[bp]:
                bp -= 1
        return max_amt

            

        