# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # tortoise and hare method from Solution tab
        # t and h both start at zero, take one step each, then loop
        t = nums[0]  # index of the next value
        h = nums[nums[0]]  # index of the value after the next value
        while t != h:
            t = nums[t]
            h = nums[nums[h]]
        # first pass over, have found meeting point
        # hare stays there but slows down, tortoise starts over
        t = 0
        while t != h:
            t = nums[t]
            h = nums[h]
        # they place they become equal is the loop point
        return t