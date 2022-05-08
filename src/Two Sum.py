# Approach 1: Brute Force
# Time complexity: O(n^2)  Space complexity O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]


# Approach 2: Two-pass HarhMap: reduce loop into search
# Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]

# Approach 3: One-pass HarhMap: Search while inserting
# Time complexity: O(n)  Space complexity: O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and i != hashmap[complement]:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i


# res = Solution().twoSum([2, 3, 4, 5], 9)
# print(res)
