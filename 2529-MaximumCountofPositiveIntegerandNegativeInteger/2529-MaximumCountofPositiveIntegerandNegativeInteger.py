class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def search_lower(nums, target):
            left = 0
            right = len(nums) - 1
            first = None
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return (first, True) if first else (left-1, False)

        def search_upper(nums, target):
            left = 0
            right = len(nums) - 1
            second = None
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    second = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return (second, True) if second else (left, False)

        lower_bound, has_0_lower = search_lower(nums, 0)

        if has_0_lower:
            negative = lower_bound
        else:
            negative = lower_bound + 1

        upper_bound, has_0_upper = search_upper(nums, 0)

        if has_0_upper:
            positive = len(nums) - upper_bound - 1
        else:
            positive = len(nums) - upper_bound


        return max(negative, positive)

