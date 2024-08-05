'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''
def findRepeatedDnaSequences(s):
    seen, res = set(), set() #seen to keep a track of sequences that we've seen before and to keep a track of repeated sequences
    for l in range(len(s) - 9):
        cur = s[l:l+10] #extract all possible 10-letter long substrings
        if cur in seen:
            res.add(cur)
        seen.add(cur)
    return list(res)


s='AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
a=findRepeatedDnaSequences(s)
print(a)
