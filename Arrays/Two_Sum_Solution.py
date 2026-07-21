# Intuition
'''Iterate through the array one element at a time. For each element, calculate the remaining value needed to reach the target (target - current_num). If the remaining value exists in the array and is at a different index, return the indices of both numbers.

# Approach
1. Traverse the array using a loop.
2. Store the current element.
3. Calculate:remaining = target - current_num
4. Check if remaining exists in the array.
5. Ensure it is not the same index.
6. Return both indices.

# Complexity
- Time complexity: O(n)
- Space complexity: O(1)'''

# Code

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i in range(len(nums)):
             current_num=nums[i] 
             remaining=target-current_num
             if remaining in nums and nums.index(remaining)!=i:
                return [i,nums.index(remaining)]     
```
