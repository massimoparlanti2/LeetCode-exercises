# Problem <3370> - Smallest Number with all set bits (Easy)
# URL: https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29
# Description:
#   You are given a positive number n.
#   Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
#
# Example 1:
#   Input: n = 5
#   Output: 7   
#   Explanation:
#   The binary representation of 7 is "111".
#
# Example 2:
#   Input: n = 10
#   Output: 15
#   Explanation:
#   The binary representation of 15 is "1111". 
#
# Example 3:
#   Input: n = 3
#   Output: 3
#   Explanation:
#   The binary representation of 3 is "11".    

def smallest_number_with_all_set_bits(n: int) -> int:
    # Find the number of bits required to represent n
    num_bits = n.bit_length()
    
    # The smallest number with all set bits greater than or equal to n
    result = (1 << num_bits) - 1
    
    return result

if __name__ == "__main__":
    test_cases = [
        (5, 7),
        (10, 15),
        (3, 3)
    ]
    
    for word1,expected in test_cases:
        result = smallest_number_with_all_set_bits(word1)
        print(f"mergeAlternately({word1}) = {result} | Expected: {expected} | Pass!!!")
        assert result == expected, "Test failed!"

# time complexity: O(1)
# space complexity: O(1)
