'''Intuition
Reverse only half of the number instead of the entire number. If the first half equals the reversed second half, the number is a palindrome. This approach is more efficient and avoids unnecessary operations.

Approach
Return False for negative numbers and numbers ending with 0 (except 0 itself).
Reverse the last half of the digits using modulo (%) and integer division (//).
Compare the first half with the reversed second half.
For odd-length numbers, ignore the middle digit by comparing x == rev // 10.

Complexity
Time complexity:O(log₁₀ n)
Space complexity:O(1)'''

# Code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10
