# Problem <1716> - Calculate Money in Leetcode bank (Easy)
# URL: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25
# Description:
#   Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#   He starts by putting in $1 on Monday, the first day. 
#   Every day from Tuesday to Sunday, he will put in $1 more than the day before. 
#   On every subsequent Monday, he will put in $1 more than the previous Monday.
#   Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
#
# Example 1:
#   Input: n = 4
#   Output: 10
#   Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
#
# Example 2:
#   Input: n = 10
#   Output: 37
#   Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. 
#   Notice that on the 2nd Monday, Hercy only puts in $2.
#
# Example 3:
#   Input: n = 20
#   Output: 96
#   Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


def totalMoney(n: int) -> int:
    full_weeks = n // 7
    remaining_days = n % 7
    sum_full_weeks = full_weeks * 28 + 7 * (full_weeks * (full_weeks - 1)) // 2 #sum of entire weeks
    sum_remaining_days = remaining_days * (remaining_days + 1) // 2 + remaining_days * full_weeks   #sum of remaining days
    
    return sum_full_weeks + sum_remaining_days


if __name__ == "__main__":
    test_cases = [
        (10, 37),
        (4, 10),
        (20, 96)
    ]
    
    for n, expected in test_cases:
        result = totalMoney(n)
        print(f"mergeAlternately({n}) = {result} | Expected: {expected} | Pass!!!")
        assert result == expected, "Test failed!"

# Time complexity: O(1), is linear
# Space complexity: O(1)
