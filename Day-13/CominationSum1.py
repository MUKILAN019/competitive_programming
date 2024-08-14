def combinationSum(candidates, target):
    def backtrack(remaining, comb, start):
        if remaining == 0:

            result.append(list(comb))
            return
        elif remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remaining - candidates[i], comb, i)
            comb.pop()
    
    result = []
    candidates.sort() 
    backtrack(target, [], 0)
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  
