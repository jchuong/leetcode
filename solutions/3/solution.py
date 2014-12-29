class Solution:
  # @return an integer
  def lengthOfLongestSubstring(self, s):
    dict = {}
    maxLen = 0
    currLen = 0
    startIdx = 0
    for idx, x in enumerate(s):
      if (x not in dict):
        dict[x] = idx
         currLen = currLen + 1
      else:
        # remove everything up to the duplicate
        dupIdx = dict[x]
        substr = s[startIdx:dupIdx]
        startIdx = dupIdx + 1
        if (maxLen < currLen):
          maxLen = currLen
        for y in substr:
          del dict[y]
        # re-add the duplicate char
        dict[x] = idx
        currLen = len(dict)
    return max(maxLen, currLen)
