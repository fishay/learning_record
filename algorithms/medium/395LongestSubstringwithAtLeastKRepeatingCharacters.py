Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
  
Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 
Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if k > len(s):
            
            # k is too large, larger than the length of s
            # Quick response for invalid k
            return 0
        
        
        # just for the convenience of self-recursion
        f = self.longestSubstring
        
        ## dictionary
        # key: unique character
        # value: occurrence
        char_occ_dict = collections.Counter(s)
        
        # Scan each unique character and check occurrence
        for character, occurrence in char_occ_dict.items():
            
            if occurrence < k:
                
                # If occurrence of current character is less than k,
                # find possible longest substring without current character in recursion
                
                return max( f(sub_string, k) for sub_string in s.split(character) )
        
        # -------------------------------
        
        # If occurrences of all characters are larger than or equal to k
        # the length of s is the answer exactly
        
        return len(s)
