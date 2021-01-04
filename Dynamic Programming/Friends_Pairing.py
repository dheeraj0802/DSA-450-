class Solution:
    def countFriendsPairings(self, n):
        # code here 
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2]*(i-1))%(10**9+7)
        return dp[-1]    
