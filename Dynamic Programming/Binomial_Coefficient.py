class Solution:
    def nCr(self, n, k):
        # code here
        m=10**9+7
        dp=[[0 for i in range(k+1)] for j in range(n+1)]
        for i in range(n+1):
            for j in range(min(i,k)+1):
                if j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%m
        return dp[-1][-1]       
