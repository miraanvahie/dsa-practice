# Contains Duplicate (LeetCode #217)
# Story: keep a notebook; walk each number; if already in notebook -> duplicate;
#        else write it down; if loop ends, no duplicate.
# Time: O(n)  Space: O(n)

def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False
