numbers = []
while True:
    num = input("Enter a number: ")
    if num == "":
        break
    numbers.append(num)

counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num in counts:
    print(num, "appears", counts[num], "times.")
