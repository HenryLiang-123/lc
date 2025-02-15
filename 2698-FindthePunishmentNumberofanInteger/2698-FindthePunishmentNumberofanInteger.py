class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isValid(start, path_sum, target):
            if path_sum > target:
                return False

            if path_sum == target and start == len(s):
                return True

            for i in range(start, len(s)):
                curr = int(s[start:(i+1)])
                if isValid(i+1, path_sum + curr, target):
                    return True

            return False


        result = 0
        for i in range(1, n+1):
            s = str(i*i)
            target = i
            if isValid(0, 0, target):
                # print(i*i)
                result += i*i

        # s = '1369'
        # print(isValid(0,0,37))

        return result

