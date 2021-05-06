Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()"
Output: true
  
Example 2:
Input: s = "()[]{}"
Output: true
  
Example 3:
Input: s = "(]"
Output: false
  
Example 4:
Input: s = "([)]"
Output: false
  
Example 5:
Input: s = "{[]}"
Output: true
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        a = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in a:
                stack.append(i)
            elif len(stack) == 0 or a[stack.pop()] != i:
                return False
        return len(stack) == 0
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket
