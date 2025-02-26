numbers = []
with open("dane.txt", "r") as file:
    for line in file:
        for num in line.split():
            numbers.append(int(num))

sum_of_numbers = sum(numbers)

print("Numbers:", numbers)
print("Sum:", sum_of_numbers)

# Numbers: [1, 3, 4, 5, 13, 2, 45, 8, 12, 13, 2, 5, 89, 3, 30, 28, 6, 14, 100, 5, 45, 87, 23, 9]
# Sum: 552