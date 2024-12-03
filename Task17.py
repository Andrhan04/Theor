

x = [ 8, 5, 4,  9,  7]
y = [10, 6, 6, 15, 12]
ans = 1
n = len(x)
for i in range(n):
    ans -= 6/(n*(n**2 - 1)) * (x[i]-y[i])**2

print(ans)