# Problem <3354> - Make array elements equal to zero (Easy)
# URL: https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-29
# Description:
#   You are given an integer array nums.
#   Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.
#   After that, you repeat the following process:
#   If curr is out of the range [0, n - 1], this process ends.
#   If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
#   Else if nums[curr] > 0:
#       Decrement nums[curr] by 1.
#       Reverse your movement direction (left becomes right and vice versa).
#       Take a step in your new direction.
#   A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
#   Return the number of possible valid selections.
#
# Example 1:
#   Input: nums = [1,0,2,0,3]
#   Output: 2
#   Explanation:
#   The only possible valid selections are the following:
#   Choose curr = 3, and a movement direction to the left.
#   [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
#   Choose curr = 3, and a movement direction to the right.
#   [1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
#
# Example 2:
#   Input: nums = [2,3,4,0,4,1,0]
#   Output: 0
#   Explanation:
#   There are no possible valid selections.

from typing import List


def count_valid_selections(nums):
    valid = 0
    
    # try from each 0 position
    for start_pos in range(len(nums)):
        if nums[start_pos] != 0:
            continue
            
        # try left direction
        sample = nums.copy()
        curr = start_pos
        direction = -1
        
        while 0 <= curr < len(nums):
            if sample[curr] == 0:
                curr += direction
                continue
            if sample[curr] > 0:
                sample[curr] -= 1
                direction *= -1
            curr += direction
            
        if all(x == 0 for x in sample):
            valid += 1
            
        # try right direction
        sample = nums.copy()
        curr = start_pos
        direction = 1
        
        while 0 <= curr < len(nums):
            if sample[curr] == 0:
                curr += direction
                continue
            if sample[curr] > 0:
                sample[curr] -= 1
                direction *= -1
            curr += direction
            
        if all(x == 0 for x in sample):
            valid += 1
            
    return valid

if __name__ == "__main__":
    test_cases = [
        ([1,0,2,0,3], 2),
        ([2,3,4,0,4,1,0], 0)
    ]
    
    for word1,expected in test_cases:
        result = count_valid_selections(word1,)
        print(f"mergeAlternately({word1}) = {result} | Expected: {expected} | Pass!!!")
        assert result == expected, "Test failed!"

# Time complexity: O(N^2), where N is the length of nums
# Space complexity: O(N) due to the copy of the nums array



