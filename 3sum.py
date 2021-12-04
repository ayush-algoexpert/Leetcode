# O(n^2) Time | O(n) Space, where n is length of nums
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for index in range(len(nums) - 2):
            firstNum = nums[index]
            target = -1 * firstNum
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    triplet = [firstNum, nums[left], nums[right]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        return triplets
