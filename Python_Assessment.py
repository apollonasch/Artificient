# Define function
def sum_of_cubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum

# Input n integer
Example_1 = sum_of_cubes(2)
Example_2 = sum_of_cubes(3)

# Print outputs
print(Example_1)
print(Example_2)