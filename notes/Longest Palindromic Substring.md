## Longest Palindromic Substring

#### Approach 1: Brute Force

The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.

**Complexity Analysis**

- Time complexity : O(n^3). Assume that n is the length of the input string, there are a total of n(n-1)/2 such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes O(n) time, the run time complexity is O(n^3).
- Space complexity : O(1).

#### Approach 2: Dynamic Programming

To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

In fact, we could solve it in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.

You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

**Complexity Analysis**

- Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
- Space complexity : O(1)

```python
# Approach 1: Dynamic Programming
# TimeComplexity O(n^2) SpaceComplexity O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
```

#### Approach 3: Manacher's Algorithm

There is even an O(n) algorithm called Manacher's algorithm, explained [here in detail](https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm). However, it is a non-trivial algorithm, and no one expects you to come up with this algorithm in a 45 minutes coding session. But, please go ahead and understand it, I promise it will be a lot of fun.