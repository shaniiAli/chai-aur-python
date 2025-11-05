def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid number.')

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


while True:
    number_of_people = get_int('How many people are in the group: ')
    if number_of_people > 0:
        break
    print("Number of people must be greater than 0.")


name_of_each_person = []
for i in range(number_of_people):
    name = input(f'Enter the name of person {i+1} :').strip()
    name_of_each_person.append(name)


total_bill = get_float('Enter the total bill amount: ')
bill_per_person = round(total_bill / number_of_people, 2)


print("\n" + "-" * 40)
print("Bill Summary")
print(f'Total Bill Amount: Rs{total_bill:.2f}')
print(f'Each Person owes: Rs{bill_per_person:.2f}')
print("*" * 40)

for name in name_of_each_person:
    print(f'{name.capitalize()} owes: Rs{bill_per_person:.2f}')

print("-" * 40)

