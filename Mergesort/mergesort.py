# Given two integer lists sorted in non-decreasing order,
# merge them into a single list sorted in non-decreasing order.

def merge(nums1: list[int], nums2: list[int]) -> list[int] :
    m = len(nums1)
    n = len(nums2)
    i,j = 0,0
    nums_merged = []

    while i < m :
        if j >= n :
            nums_merged.append(nums1[i])
            i = i+1
        elif nums1[i] <= nums2[j] :
            nums_merged.append(nums1[i])
            i = i+1
        else :
            nums_merged.append(nums2[j])
            j = j+1
    
    while j < n:
        nums_merged.append(nums2[j])
        j = j+1

    return nums_merged

lst1 = [1,3,5,6]
lst2 = [2,2,4,5]
print(merge(lst1, lst2))