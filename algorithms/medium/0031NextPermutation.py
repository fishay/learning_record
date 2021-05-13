Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
  
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
  
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
  
Example 4:
Input: nums = [1]
Output: [1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i > -1:
            if nums[i] < nums[i+1]:
                pivot = j = i+1
                while j<len(nums) and nums[i] < nums[j]:
                    pivot = j
                    j += 1
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
            i-=1
        nums[i+1:] = nums[i+1:][::-1]
