n = int(input())
a = [0]
d = [0 for x in range(n+1)]

for i in range(n):
    a.append(int(input()))

if n >= 1:
    d[1] = a[1]
    
if n >= 2:
    d[2] = a[1] + a[2]
    
if n >= 3:
    for i in range(3, n+1):
        d[i] = max(d[i-3] + a[i-1] + a[i], d[i-2] + a[i])
        
print(d[n])

