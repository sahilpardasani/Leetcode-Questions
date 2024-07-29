#Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.
# Example strs=["flower","flow","flight"] output is "fl"; strs2=['dog','cat','monkey'] output is ''.

def longest_common_prefix(lst1):
    if not lst1:
        return ""
    prefix = lst1[0]
    for s in lst1[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
