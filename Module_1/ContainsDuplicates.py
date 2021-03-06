# https://leetcode.com/problems/contains-duplicate/submissions/

# faster than 99.88% of submissions!!

class Solution:
    # if there are duplicates, the set (removes dupes) is shorter
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
