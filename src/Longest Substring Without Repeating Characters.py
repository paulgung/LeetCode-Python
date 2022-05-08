# Brute Force
# Time complexity: O(n^3)  Space complexity O(min(m,n))
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         def check(start, end):
#             chars = [0] * 128
#             for i in range(start, end + 1):
#                 if chars[ord(s[i])] == 0:
#                     chars[ord(s[i])] += 1
#                 else:
#                     return False
#             return True
#
#         res = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if check(i, j):
#                     res = max(res, j - i + 1)
#         return res

# Sliding Window
# Time complexity: O(n)  Space complexity O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = 0
        res = 0
        for right in range(len(s)):
            while chars[ord(s[right])] != 0:
                chars[ord(s[left])] -= 1
                left += 1
            chars[ord(s[right])] += 1
            res = max(res, right - left + 1)
        return res


# Sliding Window
# Time complexity: O(n)  Space complexity O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            res = max(res, right - left + 1)
        return res


# Sliding Window Optimized
# Time complexity: O(n)  Space complexity O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)
            res = max(res, j - i + 1)
            mp[s[j]] = j
        return res
