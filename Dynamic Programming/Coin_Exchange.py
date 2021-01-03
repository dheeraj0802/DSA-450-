class Solution:
    def count(self, S, m, n): 
        # code here 
        dp=[[0 for i in range(m)] for j in range(n+1)]
        for i in range(m):
            dp[0][i]=1
        for i in range(1,n+1):
            for j in range(m):
                if (i-S[j])>=0:
                    x=dp[i-S[j]][j]
                else:
                    x=0
                if (j>0):
                    y=dp[i][j-1]
                else:
                    y=0
                dp[i][j]=x+y
        return dp[n][m-1]  