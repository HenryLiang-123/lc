s = set(arr)
m1 = {}  # keeps track of (x_1, x_2)
m2 = []  # keeps track of (x_2, x_3)
idx = 0
for i in range(len(arr)):
   for j in range(i+1, len(arr)):
       if arr[i] + arr[j] in s:
           m1[(arr[i], arr[j])] = idx
           m2.append((arr[j], arr[i] + arr[j]))
           idx += 1

m3 = {}  # all edges from (x_1, x_2, x_3) to (x_2, x_3, x_4)
for i, k in enumerate(m2):
   m3[i] = m1.get(k, None)

to_remove = set()
max_l = 3 if len(m3) else 0
for k, v in m3.items():  # iterate over O(n^2) elements.
# Each element will be looked at at most twice (once during the inner while loop)
# (second time to check if it's been already looked at)
   if k in to_remove:
       continue
   l = 3
   while v is not None:
       l += 1
       to_remove.add(v)
       v = m3[v]
   if l > max_l:
       max_l = l
return max_l