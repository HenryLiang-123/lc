class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        base_to_str = defaultdict(list)
        keys = ["".join(sorted(strs[i])) for i in range(n)]

        for i in range(n):
            key, value = keys[i], strs[i]
            base_to_str[key].append(value)
        
        result = []
        for key, value in base_to_str.items():
            result.append(value)

        return result


