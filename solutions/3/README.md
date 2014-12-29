# 3 - Longest Substring Without Repeating Characters
https://oj.leetcode.com/submissions/detail/17436572/

Another fairly straightforward solution.
Immediately, bruteforce is O(n^2) in all cases.
Add one character at a time to the substring and make sure it is not a duplicate character.
If it is, remove the first character and try again.
Continue until all character combinations are completed.

Of course, you can optimize this by finding the duplicate character in the substring and move up to there.
Furthermore, note that this is just the length of the substring so we don't care about the actual substring.
Therefore, using a hash table of characters in your substring is an easy way to see if there is a duplicate

The solution I used was to insert each character into a hash table.
If the character is in the hash table, I removed every character from the substring to the first instance of the duplicate character.
Then I add the duplicate character into the hash table and continue.
Thus, this is O(n) with O(n) space.

One small optimization is once a substring has reached >= n/2 characters, there can be no longer substring. Thus when that substring hits a duplicate character,
then it has to be the longest substring. 
