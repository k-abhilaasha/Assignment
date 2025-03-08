def removeDuplicates(n):
    # Convert the list to a set to remove duplicates, then back to a list
    s = set(n)
    unique_numbers = list(s)
    
    # Return the length of the unique numbers list and the list itself
    return len(unique_numbers), unique_numbers

# Taking input from the user and converting it to a list of integers
n = list(map(int, input().split()))

# Call the removeDuplicates function and unpack the result into two variables
result, unique_numbers = removeDuplicates(n)

# Print the result
print(result, unique_numbers)