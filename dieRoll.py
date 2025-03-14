import random #For generating random numbers

#Generated the random numbers
random_numbers = [random.random() for _ in range(1000)] #A list of the 1000 random numbers between 0 and 1

frequency = {i: 0 for i in range(1, 7)} #Initialize the frequency of all 6 faces to 0
total = 0
percentage_total = 0

for number in random_numbers:
    if 0 < number < 1/6 : #Check if the random no generated lies between 0 and 1/6, increase the frequency of face 1(index 0) by 1
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
print(f"{'Face':<6}{'Frequency':<10}{'Percentage'}") #Aligning the headers with respective character spaces
print("-" * 25) #Line separator

for face, freq in frequency.items():
    percentage = (freq / 10) # calculated the % using this instead of (freq / 1000) * 100

    print(f"{face:<6}   {freq:<10}{percentage:.1f}%") #Print out the values
    percentage_total += percentage #Updating the total % after each iteration
    total += freq #Total frequency

print("-" * 25)#Line separator
print(f"{'Total:':<6}   {total:<10}{percentage_total:.1f}%") #% to 1 d.p