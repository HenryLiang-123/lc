class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # find first non-increasing digit going backwards
        # swap with first element that is larger
        digits = list(str(n))
        length = len(digits)
        i, j = length-1, length-1

        while i >= 0:
            if i == length-1:
                i -= 1
                continue
            if digits[i] < digits[i+1]:
                break
            else:
                i -= 1
        if i == -1:
            return -1

        while j >= 0:
            if digits[j] > digits[i]:
                break
            else:
                j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        sorted_part = sorted(digits[i+1:])
        digits[i+1:] = sorted_part
        result = int("".join(digits))
        if result > 2**31 - 1:
            return -1
        return result

        