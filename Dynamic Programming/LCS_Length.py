dp=[[-1 for i in range(n+1)] for j in range(m+1)]
    
    def solve(m,n,X,Y,dp):
        if dp[m][n]!=-1:
            return dp[m][n]
        if m==0 or n==0:
            return 0
        elif X[m-1]==Y[n-1]:
            
            dp[m][n]= 1+solve(m-1,n-1,X,Y,dp)
            return dp[m][n]
        else:
            dp[m][n] =  max(solve(m-1,n,X,Y,dp),solve(m,n-1,X,Y,dp))
            return dp[m][n]
    solve(m,n,X,Y,dp)
    return dp[-1][-1]
        
