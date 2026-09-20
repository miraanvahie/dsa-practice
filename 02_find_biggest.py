# Find the biggest number in a list
# Story: put first number in a box; walk each number; if bigger, replace; return box.
# Time: O(n)  Space: O(1)

def find_biggest(nums):
    biggest = nums[0]
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest
