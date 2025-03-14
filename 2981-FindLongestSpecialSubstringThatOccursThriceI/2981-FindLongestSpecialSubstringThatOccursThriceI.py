class Solution:
    def maximumLength(self, s: str) -> int:
        freq = defaultdict(int) #(char, count) -> freq
        n = len(s)

        for i in range(n):
            element = s[i]
            char_count = 1
            freq[(element, char_count)] +=1
            for j in range(i+1, n):
                if s[j] == element:
                    char_count += 1
                    freq[(element, char_count)] +=1
                else:
                    break

            # freq[(element, char_count)] +=1 
        result = float('-inf')
        for key, value in freq.items():
            if value >= 3:
                result = max(result, key[1])
        return result if result != float('-inf') else -1
            