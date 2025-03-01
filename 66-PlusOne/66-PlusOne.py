class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        result = []
        last_digit = digits[-1] + 1
        if last_digit < 10:
            digits[-1] += 1
            return digits

        carry = 1
        for i in reversed(range(n)):
            num = digits[i] + carry
            if num < 10:
                digits[i] = num
                return digits
            else:
                digits[i] = 0
        digits = [1] + digits
        return digits
            


            
