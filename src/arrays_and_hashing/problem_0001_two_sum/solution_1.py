"""
Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Topics: Array, Hash Table
"""


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            for jndex, jtem in enumerate(nums[index+1:]):
                if item+jtem == target:
                    return [index, jndex+index+1]
        

