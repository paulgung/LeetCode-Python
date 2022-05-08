## Climbing Stairs

#### General inutution

 Intution : the next distinict way of climbing stairs is euqal to the sum of the last two distinict way of climbing

distinct(n) = distinict(n-1) + distinict(n-2)

This intution can be applied using the following three approach --> ordered from easy to difficult approach

#### Idea 1 : pure recursive (Can't pass the test case :does not work for big number)

- The base case will be when only 1 or 2 steps left

- Result time-exced limit

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
         def climb(n):
             if n==1: #only one step option is availble
                 return 1
             if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             return climb(n-1) + climb(n-2)
         return climb(n)
    
```



#### Idea 2 : use dictionary (look-up table) to memorize repeating recursion

- The memory start with the base case and recored every recurssion

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo: # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)
```



#### Idea 3 : Dynamic programming

store the distinct ways in a dynamic table

climb = [climb(0), climb(1), climb(2)=climb(0)+climb(1), climb(3)=climb(2)+climb(1),......climb(n)=climb(n-1)+climb(n-2)]

dp = [ 0, 1, 2, 3, 5, dp(i-1)+dp(i-2])]

return dp[n]

```python
# Idea 3 : Dynamic programming
class Solution:
    def Factorial(self, n, m):
        # edge cases
        if n == 1: return 1
        if n == 2: return 2
        dp = [1] * (n)  # considering zero steps we need n+1 places
        dp[0] = 1
        dp[1] = 2
        for i in range(3, n + 1):
            dp[i - 1] = dp[i - 2] + dp[i - 3]
            return dp[n - 1]
```

### 

#### Idea 4: Factorial

```python
# Approach: Factorial
# TimeComplexity:O(n) SpaceComplexity:O(1)
class Solution:
    def Factorial(self, n, m):
        res = 1
        for i in range(n, m, -1):
            res = res * i
        return res

    def climbStairs(self, n: int) -> int:
        result = 0
        max_m = n // 2
        m = 0
        for n in range(n, max_m - 1, -1):
            # For n>0, n! = 1×2×3×4×...×n
            # For n=0, 0! = 1
            if m == 0:
                result += 1
                m += 1
                continue
            result += int(self.Factorial(n, n - m) / self.Factorial(m, 0))
            m += 1
        return result
```