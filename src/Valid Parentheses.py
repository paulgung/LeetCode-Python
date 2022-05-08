# Brute Force
# Time complexity: O(n)  Space complexity O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(','}':'{',']':'['}
        for i in range(len(s)):
            stack.append(s[i])
            if(s[i] in dict.keys()) and stack[len(stack)-2] == dict[s[i]]:
                stack.pop()
                stack.pop()
        if stack == []:
            return True
        else:
            return False

res = Solution().isValid('(){}[]')
print(res)