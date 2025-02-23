def gcd(a, b):
    # Using Euclid's Algorithm to calculate GCD
    while b:
        a, b = b, a % b
    return a

def lcmAndGcd(a, b):
    # Calculate GCD
    gcd_value = gcd(a, b)
    # Calculate LCM using the formula: LCM(a, b) = (a * b) // GCD(a, b)
    lcm_value = (a * b) // gcd_value
    return [lcm_value, gcd_value]

# Accept user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function and display the result
result = lcmAndGcd(a, b)
print(result)