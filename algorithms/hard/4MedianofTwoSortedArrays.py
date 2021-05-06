Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
  
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
  
Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
  
Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000
  
Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Follow up: The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        n1,n2 = len(nums1),len(nums2)
        if n1 == 0:
            return (nums2[int((n2-1)/2)] + nums2[int(n2/2)])/2
        leftHalf = (n1+n2+1)//2
        minContribution = 0
        maxContribution = n1
        
        while minContribution <= maxContribution:
            cut1 = int((minContribution + maxContribution)/2)
            cut2 = int(leftHalf - cut1)
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            if (l1 > r2):
                maxContribution = cut1 - 1
            elif (l2 > r1):
                minContribution = cut1 + 1
            else:
                if ((n1 + n2)%2 == 0):
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
