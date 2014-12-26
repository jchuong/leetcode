# 1 - Two Sum
https://oj.leetcode.com/problems/two-sum/

Things to remember:
1. Exactly one solution
2. Indexes are not zero-based
3. The numbers are not ordered by size
4. Index 1 < index 2

So #3 and #4 are an issue since it would be nice to sort the array, but you would lose the indexes.  You could either copy the array with indexes (key-value pair but it doesn't say anything about duplicate values).  Or, search for the number afterwards (linear since numbers are not ordered by size).

The brute force solution would be to take each number, and try every other number.  This is n * (n - 1) + (n - 1) * (n - 2) + ... + (n - (n - 2)) * (n - (n - 1) ) which is O(n^2).  This brute force times out on leetcode.

So it should be better to sort the array in O(nlogn).  Let's try using the search method at the end to find the indicies O(log n) on the sorted array, or O(n) on the unsorted array. 

Another thing to consider is filtering numbers that are larger than the target.  That is potentially O(n) if you do it separately.  Numpy has a threshold splice but imports are forbidden on leetcode.  However, this is actually not possible since numbers can be negative.

So the current solution is to sort the array, brute force the combination and then find the index:
O(nlogn) + O(n^2) + O(n)

While it is O(n^2), there is early termination in the average case.  One wrost case would be all negative numbers with one large number that adds to the target.

The current runtime of this solution is: *192ms*
