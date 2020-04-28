# https://leetcode.com/problems/two-sum/submissions/

# first pass:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index2 in range(index+1, len(nums)):
                if value + nums[index2] == target:
                    return [index, index2]