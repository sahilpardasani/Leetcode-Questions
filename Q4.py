#Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

def getCommon(nums1, nums2):
    set1=set(nums1)
    set2=set(nums2)
    common_elements= set1.intersection(set2)
    if common_elements:
        return min(common_elements)
    else:
        return -1 
          
nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))
