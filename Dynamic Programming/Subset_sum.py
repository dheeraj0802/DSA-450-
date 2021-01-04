class Solution:
    def equalPartition(self, N, arr):
        # code here
        x=sum(arr)
        if x%2==1:
            return 0
        x=x//2
        dp=[[False for i in range(N+1)] for j in range(x+1)]
        for i in range(x+1):
            for j in range(N+1):
                if i==0:
                    dp[i][j]=True
                elif j==0:
                    dp[i][j]=False
                elif arr[j-1]>i:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=dp[i-arr[j-1]][j-1] or dp[i][j-1]
        if dp[-1][-1]:
            return 1
        return 0    
