import random #For generating random numbers

#Define the random number generated
random_numbers = [random.random() for _ in range(1000)] #A list of the 100 random numbers

#Frequency of occurrence of a face
frequency = {i: 0 for i in range(1, 7)} #for the 6 faces
total = 0
percentage_total = 0

for number in random_numbers:
    if 0 < number < 1/6 : #if the no lies between 0 and 1/6, increase the frequency of face 1(index 0) by 1
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

#Results
print(f"{'Face':<5}{'Frequency':<10}{'Percentage'}")
print("-" * 25)
for face, freq in frequency.items():
    percentage = (freq / 10) # instead of (freq / 1000) * 100
    print(f"{face:<5}   {freq:<10}{percentage:.1f}%")
    percentage_total += percentage
    total += freq

print("-" * 25)
print(f"{'Total:':<5}   {total:<10}{percentage_total:.1f}%")