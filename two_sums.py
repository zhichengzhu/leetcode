"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = sorted(range(len(nums)), key=lambda index: nums[index])
        start_index = 0
        end_index = len(indeces) - 1
        result: List[int] = list()
        while start_index < end_index:
            sum = nums[indeces[start_index]] + nums[indeces[end_index]]
            if sum < target:
                start_index += 1
            elif sum > target:
                end_index -= 1
            else:
                result.append(indeces[start_index])
                result.append(indeces[end_index])
                break
        return result


class Tests(unittest.TestCase):
    def test_basic(self):
        solution = Solution()
        self.assertListEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])


if __name__ == "__main__":
    unittest.main()
