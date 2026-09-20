# Two Sum (LeetCode #1)
# Story: keep a notebook of number -> position; for each number find its partner
#        (target - num); if partner already seen, return both positions; else store it.
# Time: O(n)  Space: O(n)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
