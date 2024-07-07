def check_verification_number(nums):
    return sum(x**2 for x in nums) % 10

nums = [0, 4, 2, 5, 6]
print(check_verification_number(nums))  
