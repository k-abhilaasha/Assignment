def removeDuplicates(n):  
    # If the array is empty or has only one element, no duplicates to remove
    if len(n) <= 1:
        return len(n)

    i = 0  # Pointer to track the position of unique elements

    # Start from the second element (index 1)
    for j in range(1, len(n)):
        # If the current element is different from the last unique element, update the array
        if n[i] != n[j]:
            i += 1
            n[i] = n[j]  # Move the unique element to the next position

    return i + 1,n[:i+1] # Return the number of unique elements

n = list(map(int, input().split()))  # Taking input as a list of integers
result,unique_numbers= removeDuplicates(n)  # Call the function to remove duplicates
print(result,unique_numbers)  # Print the result