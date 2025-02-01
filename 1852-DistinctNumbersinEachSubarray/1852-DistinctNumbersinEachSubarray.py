class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        distinct_set = {}
        result = []
        for i in range(k):
            if nums[i] in distinct_set:
                distinct_set[nums[i]] += 1
            else:
                distinct_set[nums[i]] = 1
            # distinct_set.add(nums[i])

        result.append(len(distinct_set))
        for right in range(k, n):
            distinct_set[nums[right]] = distinct_set.get(nums[right], 0) + 1
            distinct_set[nums[left]] -= 1
            if distinct_set[nums[left]] == 0:
                del distinct_set[nums[left]]

            left += 1
            result.append(len(distinct_set))

        return result

        