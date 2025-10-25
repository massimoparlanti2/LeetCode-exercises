# Problem <1768> - Merge Strings Alternately (Easy)
# URL: 
# Description:
#   You are given two strings word1 and word2. 
#   Merge the strings by adding letters in alternating order, starting with word1. 
#   If a string is longer than the other, append the additional letters onto the end of the merged string.
#   Return the merged string.

# Example 1:
#   Input: word1 = "abc", word2 = "pqr"
#   Output: "apbqcr"
#   Explanation: The merged string will be merged as so:
#   word1:  a   b   c
#   word2:    p   q   r
#   merged: a p b q c r

# Example 2:
#   Input: word1 = "ab", word2 = "pqrs"
#   Output: "apbqrs"
#   Explanation: Notice that as word2 is longer, "rs" is appended to the end.
#   word1:  a   b 
#   word2:    p   q   r   s
#   merged: a p b q   r   s

# Example 3:
#   Input: word1 = "abcd", word2 = "pq"
#   Output: "apbqcd"
#   Explanation: Notice that as word1 is longer, "cd" is appended to the end.
#   word1:  a   b   c   d
#   word2:    p   q 
#   merged: a p b q c   d

def mergeAlternately(word1: str, word2: str) -> str:
    merged = ''.join(x + y for x, y in zip(word1, word2))
    merged += word1[len(word2):] + word2[len(word1):]
    return merged

if __name__ == "__main__":
    test_cases = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd")
    ]
    
    for word1, word2, expected in test_cases:
        result = mergeAlternately(word1, word2)
        print(f"mergeAlternately({word1}, {word2}) = {result} | Expected: {expected} | Pass!!!")
        assert result == expected, "Test failed!"

# Time complexity: O(n + m), where n and m are the lengths of word1 and word2
# Space complexity: O(n + m)
