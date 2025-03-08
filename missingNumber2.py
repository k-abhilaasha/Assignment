def missingNumber(n):
    # Sort the list to make sure it's in ascending order
    sorted_list = sorted(n)

    # Check the missing number by comparing the sorted list
    for i in range(len(sorted_list)):
        if sorted_list[i] != i:
            return i
    
    # If no missing number is found within the range, return len(n), which is the missing number
    return len(n)

# Input the list of integers
n = list(map(int, input().split()))

# Find the missing number
result = missingNumber(n)

# Print the result
print(result)