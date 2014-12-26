class Solution:
  # @return a tuple, (index1, index2)
  def twoSum(self, num, target):
    # Sort the numbers
    valid = list(num);
    valid.sort()

    value1 = 0;
    value2 = 0;
    finished = False;
    # Now brute force solutions
    for x in valid:
      for y in valid[1:]:
        if (x + y > target):
          break;
        elif (x + y == target):
          value1 = x;
          value2 = y;
          finished = True;
          break;
      if finished:
        break;

    # Now we find the indicies and we are done
    index1 = -1;
    index2 = -1;
    for idx, val in enumerate(num):
      if (val == value1 or val == value2):
        if (index1 != -1):
          # Since both indicies are found, we are finished
          index2 = idx + 1;
          break;
        else:
          # Index1 is filled in first
          index1 = idx + 1;

    return index1, index2
