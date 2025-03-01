class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        n = len(s)
        for i in range(n-10+1):
            curr_s = s[i:i+10]
            if curr_s in seen:
                result.add(curr_s)
            seen.add(curr_s)

        return list(result)