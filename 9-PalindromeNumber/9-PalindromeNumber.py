class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []

        if x < 0:
            return False
        
        while x > 0:
            digit = x % 10
            nums.append(digit)
            x = x // 10

        return nums == nums[::-1]
