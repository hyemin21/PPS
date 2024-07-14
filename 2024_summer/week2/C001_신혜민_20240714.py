def subsetXORSum(nums: List[int]) -> int:
    def dfs(i, current):
        if i == len(nums):
            return current
        return dfs(i + 1, current) + dfs(i + 1, current ^ nums[i])
    
    return dfs(0, 0)
