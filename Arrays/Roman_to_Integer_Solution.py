'''Intuition:
Instead of checking subtraction cases (IV, IX, XL, etc.) during iteration, first replace them with their additive equivalents (e.g., IV → IIII, IX → VIIII). After replacement, every Roman numeral can be processed by simply summing the value of each character.

Approach:
1. Store the value of each Roman numeral in a dictionary.
2. Replace all subtraction cases (IV, IX, XL, XC, CD, CM) with their additive forms.
3. Traverse the modified string character by character.
4. Add the corresponding value of each Roman numeral to the result.
5. Return the final sum.

Complexity
Time complexity:O(n), where n is the length of the Roman numeral string.
Space complexity:O(1), since the dictionary size is fixed and does not depend on the input size.'''

#Code
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += Roman[char]
        return number
        
