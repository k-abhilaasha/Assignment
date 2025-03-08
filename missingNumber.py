def missingNumber(n):
    # The formula for the sum of the first n natural numbers (including 0 to n)
    total_sum = (len(n) * (len(n) + 1)) // 2
    actual_sum = sum(n)
    
    # The missing number is the difference between the expected sum and the actual sum
    return total_sum - actual_sum

# Take input and convert it to a list of integers
n = list(map(int, input().split()))

# Find the missing number
result = missingNumber(n)

# Print the result
print(result)