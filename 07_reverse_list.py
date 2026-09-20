# Reverse a list in place (two pointers)
# Story: one finger at each end; while left < right, swap them, move both inward.
# Time: O(n)  Space: O(1)

def reverse_nos(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
