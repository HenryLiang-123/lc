// Last updated: 3/12/2025, 4:52:15 PM
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def is_vowel(element):
            return element in set(['a', 'e', 'i', 'o', 'u'])

        def is_valid(d, count_const, k):
            for key, value in d.items():
                if value < 1:
                    return False

            return count_const >= k

        
        def solve(k):
            left = 0
            d = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0} # vowel -> count
            consonant = 0
            result = 0
            for right in range(n):
                if is_vowel(word[right]):
                    d[word[right]] += 1
                else:
                    consonant += 1

                # if consonant > k:
                #     while left < right and consonant > k:
                #         if is_vowel(word[left]):
                #             d[word[left]] -= 1
                #         else:
                #             consonant -= 1 
                #         left += 1

                # else:
                while left < right and is_valid(d, consonant, k):
                    result += len(word) - right
                    if is_vowel(word[left]):
                        d[word[left]] -= 1
                    else:
                        consonant -= 1 
                    left += 1

            return result
        # print(solve(k), solve(k+1))
        return solve(k) - solve(k+1)


        
            
