def sfib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return(sfib(n-1)**2 + (n-2)**2)%47
print(sfib(6))

#iterative
n=int(input())
x = [1,1]
for i in range(2,n+1):
    ans = (x[i-1]**2 +(i-2)**2)%47
    x.append(ans)
print(x[n])    