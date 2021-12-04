# O(n) Time | O(1) Space, where n is length of s
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniqueChars = {}
        maxSubstringLength = 0
        currSubstringLength = 0
        for index in range(len(s)):
            char = s[index]
            if char in uniqueChars:
                uniqueChars = self.removeCharsBeforeIndex(uniqueChars[char], uniqueChars)
                maxSubstringLength = max(maxSubstringLength, currSubstringLength)
                uniqueChars[char] = index
                currSubstringLength = len(uniqueChars)
            else:
                uniqueChars[char] = index
                currSubstringLength += 1
        return max(maxSubstringLength, currSubstringLength)
    
    def removeCharsBeforeIndex(self, index, uniqueChars):
        charsToDelete = []
        for uniqueChar in uniqueChars:
            if uniqueChars[uniqueChar] <= index:
                charsToDelete.append(uniqueChar)
        for char in charsToDelete:
            del uniqueChars[char]
        return uniqueChars
