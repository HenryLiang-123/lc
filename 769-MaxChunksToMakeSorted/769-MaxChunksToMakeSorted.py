class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # use a stack. If next element is smaller than top in stack, we pop while the condition is true, and we keep the max popped element
        stack = [arr[0]]
        max_top = arr[0]
        n = len(arr)

        for i in range(1, n):
            if arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                while stack and arr[i] < stack[-1]:
                    top = stack.pop()
                    max_top = max(top, max_top)
                stack.append(max_top)

        return len(stack)

