# Given a string s, find the length of the longest substring without repeating characters. Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    chSet=set()
    l=0
    res=0

    for r in range(len(s)): #len=5
        while s[r] in chSet: # current window is invalid    
            chSet.remove(s[l])
            l+=1
        chSet.add(s[r])
        res=max(res, r-l+1)
    return res

s='abcabcbcc'
print(lengthOfLongestSubstring(s))
#Space and time complexity is O(n)
