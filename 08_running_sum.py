# Running Sum of 1d Array (LeetCode #1480)
# Story: jar starts at 0 and a result list; walk each number; add to jar;
#        append jar to result; return result.
# Time: O(n)  Space: O(n)

def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total = total + num
        result.append(total)
    return result
