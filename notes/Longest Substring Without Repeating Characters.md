## Longest Substring Without Repeating Characters

#### Approach 1: Brute Force

Check all the substring one by one to see if it has no duplicate character.

1. To enumerate all substrings of a given string, we enumerate the start and end indices of them. Suppose the start and end indices are i and j, respectively. Then we have 0≤*i*<*j*≤*n* (here end index j is exclusive by convention). Thus, using two nested loops with i from 0 to n - 1 and j from i+1 to n, we can enumerate all the substrings of `s`.
2. To check if one string has duplicate characters, we can use a set. We iterate through all the characters in the string and put them into the `set` one by one. Before putting one character, we check if the set already contains it. If so, we return `false`. After the loop, we return `true`.

```python
# Brute Force
# Time complexity: O(n^3)  Space complexity O(min(m,n))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            arr = [0] * 128
            for i in range(start, end + 1):
                if arr[ord(s[i])] == 0:
                    arr[ord(s[i])] += 1
                else:
                    return False
            return True

        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res
```



#### Approach 2: Sliding Window

To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2) algorithm. But we can do better.

By using HashSet as a sliding window, checking if a character in the current can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i, j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1) (left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current window [i, j) (j = i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in chars :
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            res = max(res, right - left + 1)
        return res
```



#### Approach 3: Sliding Window Optimized

The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.

The reason is that if s[j] have a duplicate in the range [i, j) with index j, we don't need to increase i little by little. We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.

```python
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
```