class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 0
        result = []
        while i < n and j < m:
            id_1, val_1 = nums1[i]
            id_2, val_2 = nums2[j]

            if id_1 == id_2:
                result.append([id_1, val_1 + val_2])
                i += 1
                j += 1
            elif id_1 > id_2:
                result.append([id_2, val_2])
                j += 1
            else:
                result.append([id_1, val_1])
                i += 1

        if j < m:
            result.extend(nums2[j:])
        
        if i < n:
            result.extend(nums1[i:])

        return result
