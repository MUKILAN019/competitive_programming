def count_subsequences(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1 
    last_pos = {}
    
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        
        if s[i - 1] in last_pos:
            dp[i] -= dp[last_pos[s[i - 1]] - 1]
        
        last_pos[s[i - 1]] = i
    
    return dp[n]

def better_str(a, b):
    count_a = count_subsequences(a)
    count_b = count_subsequences(b)
    
    if count_a >= count_b:
        return a
    else:
        return b


a = "gfg"
b = "ggg"
print(better_str(a, b))  


a = "a"
b = "b"
print(better_str(a, b)) 
