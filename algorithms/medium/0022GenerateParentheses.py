Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
  
Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        result = []
        self.helper(n,n,'',result)
        return result
    
    def helper(self,l,r,string,result):
        if r < l: return
        if l == 0 and r == 0:
            result.append(string)
        if l:
            self.helper(l-1,r,string+'(',result)
        if r:
            self.helper(l,r-1,string+')',result)
