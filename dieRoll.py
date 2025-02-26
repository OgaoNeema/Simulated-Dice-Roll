import random

#Define the random number generated
random_numbers = [random.random() for _ in range(1000)]

#Frequency of occurrence of a face
frequency = {i: 0 for i in range(1, 7)}

for number in random_numbers:
    if 0 < number < 1/6 :
        frequency[1] += 1
    elif 1/6 < number < 2/6:
        frequency[2] += 1
    elif 2/6 < number < 3/6:
        frequency[3] += 1
    elif 3/6 < number < 4/6:
        frequency[4] += 1
    elif 4/6 < number < 5/6:
        frequency[5] += 1
    else:
        frequency[6] += 1

total = 0
percentage_total = 0

#Results
print(f"{'Face':<5}{'Frequency':<10}{'Percentage'}")
print("-" * 25)
for face, freq in frequency.items():
    percentage = (freq / 1000) * 100
    print(f"{face:<5}   {freq:<10}{percentage:.1f}%")
    percentage_total += percentage
    total += freq

print(f"{'Total:'} {total}      {percentage_total:.1f}%")