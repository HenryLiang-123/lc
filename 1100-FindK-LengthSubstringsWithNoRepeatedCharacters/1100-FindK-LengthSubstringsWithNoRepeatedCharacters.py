class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        if k > n:
            return 0

        left = 0
        result = 0
        for right in range(n):
            window_size = right - left + 1
            freq[s[right]] += 1

            if freq[s[right]] > 1:
                while left <= right and freq[s[right]] > 1:
                    window_size -= 1
                    freq[s[left]] -= 1
                    left += 1
                    
            elif window_size == k:
                freq[s[left]] -= 1
                result += 1
                left += 1

        
                


        return result