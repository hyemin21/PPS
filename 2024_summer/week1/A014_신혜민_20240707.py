def summaryRanges(nums):
    ranges = []
    if not nums:
        return ranges
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            ranges.append(f"{start}->{nums[i - 1]}" if start != nums[i - 1] else f"{start}")
            start = nums[i]
    ranges.append(f"{start}->{nums[-1]}" if start != nums[-1] else f"{start}")
    return ranges

nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))  
