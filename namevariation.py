first = input("What is the first name? ")
middle = input("What is the middle name? ")
last = input("What is the last name? ")

first_initial = first[0]
middle_initial = middle[0]
last_initial = last[0]

first_initial_period = first_initial
middle_initial_period = middle_initial
last_initial_period = last_initial

name_list = [
first + middle + last,
first + middle + last_initial,
first + middle_initial + last,
first + middle_initial + last_initial,
first + last + middle,
first + last + middle_initial,
first + last_initial + middle,
first + last_initial + middle_initial,
last + first + middle,
last + first + middle_initial,
last + first_initial + middle,
last + first_initial + middle_initial,
last + middle + first,
last + middle + first_initial,
last + middle_initial + first,
last + middle_initial + first_initial,
middle + first + last,
middle + first + last_initial,
middle + first_initial + last,
middle + first_initial + last_initial,
middle + last + first,
middle + last + first_initial,
middle + last_initial + first,
middle + last_initial + first,
first_initial + middle + last,
first_initial + middle + last_initial,
first_initial + middle_initial + last,
first_initial + middle_initial + last_initial,
first_initial + last + middle,
first_initial + last + middle_initial,
first_initial + last_initial + middle,
first_initial + last_initial + middle_initial,
middle_initial + first + last,
middle_initial + first + last_initial,
middle_initial + first_initial + last,
middle_initial + first_initial + last_initial,
middle_initial + last + first,
middle_initial + last + first_initial,
middle_initial + last_initial + first,
middle_initial + last_initial + first_initial,
last_initial + first + middle,
last_initial + first + middle_initial,
last_initial + first_initial + middle,
last_initial + first_initial + middle_initial,
last_initial + middle + first,
last_initial + middle + first_initial,
last_initial + middle_initial + first,
last_initial + middle_initial + first_initial,
]

print(*name_list, sep="\n")
with open("names.csv", 'w') as output:
    for row in name_list:
        output.write(str(row) + '\n')
with open("names.txt", 'w') as output:
    for row in name_list:
        output.write(str(row) + '\n')
