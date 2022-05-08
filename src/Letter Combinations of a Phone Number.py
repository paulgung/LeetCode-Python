import copy


# Brute Force
# TimeComplexity:O(4^n) SpaceComplexity:O(1)
class Solution:
    def letterCombinations(self, digits):
        myMap = {"2": "abc", "3": "def",
                 "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs",
                 "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []
        myList = [""]
        res = [""]
        for i in digits:
            # e.g. digits="23"
            list = myMap[i]
            for j in myList:
                for k in list:
                    res.append(j + k)
                res.pop(0)
            # myList = copy.deepcopy(res)
            myList = res[:]
        return res


# Recursive way
# TimeComplexity:O(4^n) SpaceComplexity:O(1)
class Solution:
    def letterCombinations(self, digits):
        myMap = {"2": "abc", "3": "def",
                 "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs",
                 "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(i, curstr):
            if (i == len(digits)):
                res.append(curstr)
                return
            for c in myMap[digits[i]]:
                backtrack(i + 1, curstr + c)

        if digits:
            backtrack(0, "")
        return res


print(Solution().letterCombinations("34"))
