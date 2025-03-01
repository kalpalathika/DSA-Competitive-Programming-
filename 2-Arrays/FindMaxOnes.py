"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

link - https://leetcode.com/problems/max-consecutive-ones/description/ 
"""

from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOneCount = 0
        largestCountYet = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                maxOneCount += 1
                if(maxOneCount > largestCountYet):
                    largestCountYet = maxOneCount
            else:
                maxOneCount = 0
        return largestCountYet