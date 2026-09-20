# Count how many numbers are bigger than 10
# Story: counter starts at 0; walk each number; if > 10, add 1; return counter.
# Time: O(n)  Space: O(1)

def count_over_10(nums):
    count = 0
    for num in nums:
        if num > 10:
            count += 1
    return count
