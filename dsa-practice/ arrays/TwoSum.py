"""
Two Sum Problem

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

# ==================================
#  Approach 1: Brute Force (O(n²))
# ==================================

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))

"""
Final Complexity - Brute Force:
| Metric | Value |
|--------|-------|
| Time   | O(n²) |
| Space  | O(1)  |
"""

# ========================================
#  Approach 2: Hash Map (Optimized O(n))
# ========================================

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # num: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))

"""
Final Complexity - Hash Map:
| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |
"""
