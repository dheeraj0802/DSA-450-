def solve(x,y,n,m,dp):
    if dp[n][m]!=-1:
        return dp[n][m]
    if n==0 or m==0:
        dp[n][m]=0
        return dp[n][m]
    elif m!=n and x[m-1]==y[n-1]:
        dp[n][m]= 1+solve(x,y,n-1,m-1,dp)
        return dp[n][m]
    else:
        dp[n][m] = max(solve(x,y,n-1,m,dp),solve(x,y,n,m-1,dp))
        return dp[n][m]

t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=input()
    dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    
    x=solve(a,a[::-1],n,n,dp)
    if x>=2:
        print(x)
    else:
        print(0)
