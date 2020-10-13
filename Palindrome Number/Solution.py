class Solution:
    def isPalindrome(self, x: int) -> bool:
        initial_x = x
        if x < 0:
            return False

        mirror = 0
        while x:
            last_digit = x % 10
            mirror = mirror*10 + last_digit
            x = x//10
        
        return initial_x == mirror
