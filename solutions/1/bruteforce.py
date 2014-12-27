# Brute force, times out
class Solution:
  # @return a tuple, (index1, index2)
  def twoSum(self, num, target):
    # Now brute force solutions
    enumerated = enumerate(list(num))
    for x_idx, x in (enumerated):
      enumeratedy = enumerate(list(num[x_idx + 1:]))
      for y_idx, y in (enumeratedy):
        if (x + y == target):
          index1 = x_idx + 1
          index2 = y_idx + index1 + 1
          return index1, index2


sol = Solution()
print sol.twoSum([3,2,4], 6)
