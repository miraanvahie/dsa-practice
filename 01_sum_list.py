# Sum of a list
# Story: a jar starts at 0; walk each number; add it to the jar; return the jar.
# Time: O(n)  Space: O(1)

def sum_list(nums):
    total = 0
    for num in nums:
        total = total + num
    return total
