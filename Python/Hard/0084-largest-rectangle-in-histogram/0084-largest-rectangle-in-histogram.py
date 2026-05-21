class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        # Add a sentinel bar of height 0
        heights.append(0)

        for i, h in enumerate(heights):
            # Process taller bars
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                # Width calculation
                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area