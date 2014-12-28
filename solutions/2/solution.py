# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    carry = 0;
    result = None
    curr = None
    while (True):
      if (l1 == None and l2 == None):
        if (carry == 1):
          curr.next = ListNode(1)
        break
      val = 0
      if (l1 == None):
        val = l2.val + carry
        if (val > 9):
          carry = 1
          val = val % 10
        else:
          carry = 0
        l2 = l2.next
      elif (l2 == None):
        val = l1.val + carry
        if (val > 9):
          carry = 1
          val = val % 10
        else:
          carry = 0
        l1 = l1.next
      else:
        val = l1.val + l2.val + carry
        if (val > 9):
          carry = 1
          val = val % 10
        else:
          carry = 0
        l1 = l1.next
        l2 = l2.next

      node = ListNode(val)
      if (result == None):
        result = node
        curr = node
      else:
        curr.next = node
        curr = curr.next
    return result    
