def combinationSum2(candidates, target):
    def backtrack(remaining, comb, start):
        if remaining == 0:

            result.append(list(comb))
            return
        elif remaining < 0:

            return
        
        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            comb.append(candidates[i])

            backtrack(remaining - candidates[i], comb, i + 1)

            comb.pop()
    
    result = []
    candidates.sort()  
    backtrack(target, [], 0)
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))  

