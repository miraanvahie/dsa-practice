# Sum only the even numbers
# Story: jar starts at 0; walk each number; if even (num % 2 == 0), add it; return jar.
# Time: O(n)  Space: O(1)

def sum_evens(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total = total + num
    return total
