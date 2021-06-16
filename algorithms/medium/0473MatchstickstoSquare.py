ou are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
  
Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:
1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 10^9

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False  
        total = sum(matchsticks)
        if total%4 != 0: return False
        side = total/4
        matchsticks.sort(reverse=True)
        def dfs(a,b,c,d,e):
            if e==len(matchsticks):
                if a==b==c==d: return True
                else: return False
            m = matchsticks[e]
            if a+m <= side and dfs(a+m,b,c,d,e+1): return True
            if b+m <= side and dfs(a,b+m,c,d,e+1): return True
            if c+m <= side and dfs(a,b,c+m,d,e+1): return True
            if d+m <= side and dfs(a,b,c,d+m,e+1): return True
            return False
        return dfs(0,0,0,0,0)
