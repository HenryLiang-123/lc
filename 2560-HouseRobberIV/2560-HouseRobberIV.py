// Last updated: 3/15/2025, 1:57:58 PM
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def is_valid(capability):
            idx = []
            for i in range(n):
                if nums[i] < capability:
                    if len(idx) > 0:
                        if idx[-1] + 1 != i:
                            idx.append(i)
                    else:
                        idx.append(i)

            # if len(idx) == 2:
            #     print((idx[1] - idx[0])>1)
            #     return (idx[1] - idx[0]) > 1
            
            return len(idx) >= k

        left = min(nums)
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid -1
            else:
                left = mid + 1

        return left-1
                
