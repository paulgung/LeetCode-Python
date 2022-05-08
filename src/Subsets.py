# # Approach 1: Cascading
# # TimeComplexity O(n*2^N) SpaceComplexity O(n*2^N)
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         output = [[]]
#         for num in nums:
#             output += [curr + [num] for curr in output]
#         return output
#
#
# # Approach 2: Backtracking
# # TimeComplexity O(n*2^N) SpaceComplexity O(n)
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first=0, curr=[]):
#             # if the combination is done
#             if len(curr) == k:
#                 output.append(curr[:])
#                 return
#             for i in range(first, n):
#                 # add nums[i] into the current combination
#                 curr.append(nums[i])
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
#
#         output = []
#         n = len(nums)
#         for k in range(n + 1):
#             backtrack()
#         return output


# Approach 3: Lexicographic (Binary Sorted) Subsets
# TimeComplexity O(n*2^N) SpaceComplexity O(n*2^N)
class Solution:
    def subsets(self, nums):
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(len(bitmask)) if bitmask[j] == "1"])

        return output


Solution().subsets([1, 2, 3, 4, 5])
