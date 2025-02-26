numbers = []
sums = []
with open("dane.txt", "r") as file:
    for line in file:
        line_numbers = []
        
        for num in line.split():
            line_numbers.append(int(num))
        
        numbers.append(line_numbers)
        sums.append(sum(line_numbers))

sum_of_sums = sum(sums)
average_of_sums = int(sum_of_sums/len(sums))

print("Numbers:", numbers)
print("Sums:", sums)
print("Sum of sums:", sum_of_sums)
print("Average of sums:", average_of_sums)

# Numbers: [[1, 3], [4, 5], [13, 2], [45, 8], [12, 13], [2, 5], [89, 3], [30, 28], [6, 14], [100, 5], [45, 87], [23, 9]]
# Sums: [4, 9, 15, 53, 25, 7, 92, 58, 20, 105, 132, 32]
# Sum of sums: 552
# Average of sums: 46