first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + ' ' + last_name
address = input("Enter your address: ")
address += input('Enter the address to be added: ')
employee_age = int(input("Enter your age: "))
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = int(input("Enter your years of experience: "))
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = input("Enter the position: ")
salary = int(input("Enter the salary: "))
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = input("Enter the employee code: ")
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:]
print(last_three)
