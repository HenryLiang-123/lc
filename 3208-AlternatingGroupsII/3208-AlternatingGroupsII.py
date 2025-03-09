class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        arr = colors + colors[:k-1]
        print(arr)
        n = len(arr)
        left = 0
        result = 0
        for right in range(1, n):   
            window_size = right-left+1
            
            if arr[right-1] == arr[right]:
                left = right
            elif window_size == k:
                result += 1
                left += 1

        return result


