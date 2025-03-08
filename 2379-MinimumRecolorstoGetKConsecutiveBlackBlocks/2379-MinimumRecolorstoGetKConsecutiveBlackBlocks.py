class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left = 0
        counts = {"B":0, "W":0}
        result = float('inf')
        for right in range(n):
            window_size = right - left + 1
            counts[blocks[right]] += 1
            if window_size == k:
                result = min(result, counts['W'])
                counts[blocks[left]] -= 1
                left += 1

        return result



