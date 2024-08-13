def count_subsets_with_given_sum(arr, n, target_sum):
    MOD = 10**9 + 7
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            dp[i][j] = dp[i-1][j]  
            if arr[i-1] <= j:
                dp[i][j] = (dp[i][j] + dp[i-1][j-arr[i-1]]) % MOD  
    return dp[n][target_sum]
n = 6
arr = [5, 2, 3, 10, 6, 8]
target_sum = 10
print(count_subsets_with_given_sum(arr, n, target_sum)) 
