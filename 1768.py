## MERGE STRINGS ALTERNATELY

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
    l1=len(word1)
    l2=len(word2)
    i=0
    final=""
    for x,j in zip(word1,word2):
        final+=x + j

    final += word1[len(word2):] + word2[len(word1):]
    return final


a="abc"
b="pqr"
f=mergeAlternately(a,b)
print(f)

a="ab"
b="pqrs"
f=mergeAlternately(a,b)
print(f)

a="abcd"
b="pq"
f=mergeAlternately(a,b)
print(f)