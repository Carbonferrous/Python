m = 3
a = [1] * m + [2]
for n in range(m+1, 50+1):
    a += [a[n-1] + sum(a[j] for j in range(n-m)) + 1]
print(a[50])
