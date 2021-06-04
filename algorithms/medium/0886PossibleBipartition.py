Given a set of n people (numbered 1, 2, ..., n), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
  
Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
  
Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_table = collections.defaultdict(list)
        for a,b in dislikes:
            dislike_table[a].append(b)
            dislike_table[b].append(a)
        
        color_table = [ None for _ in range(n+1) ]
        
        def dfs(num, color):
            if not color_table[num]:
                color_table[num] = color
            else:
                return color_table[num] == color
            
            for other in dislike_table[num]:
                if not dfs(other, 2 if color==1 else 1):
                    return False
            return True
        
        for num in range(1,n+1):
            if not color_table[num] and not dfs(num,1):
                return False
        return True
