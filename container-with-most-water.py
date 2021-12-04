class Solution(object):
    # O(n) Time | O(1) Space, where n is length of height
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        leftIdx = 0
        rightIdx = len(height) - 1
        while leftIdx < rightIdx:
            currWater = self.getArea(leftIdx, rightIdx, height)
            maxWater = max(maxWater, currWater)
            if height[leftIdx] > height[rightIdx]:
                rightIdx -= 1
            elif height[leftIdx] < height[rightIdx]:
                leftIdx += 1
            else:
                leftIdx += 1
                rightIdx -= 1
        return maxWater
        
        
    def getArea(self, indexOne, indexTwo, heights):
        heightOne = heights[indexOne]
        heightTwo = heights[indexTwo]
        
        breadth = indexTwo - indexOne
        length = min(heightOne, heightTwo)
        return length * breadth
