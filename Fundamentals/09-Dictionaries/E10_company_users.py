# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each
# employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# •	The input always will be valid.

command = input()

companies_info = {}

while command != 'End':
    employee_info = command.split(' -> ')
    company_name = employee_info[0]
    employee_id = employee_info[1]

    if company_name not in companies_info.keys():
        companies_info[company_name] = []

    if employee_id not in companies_info[company_name]:
        companies_info[company_name].append(employee_id)

    command = input()

for company in companies_info.keys():
    print(f'{company}')
    for employee_id in companies_info[company]:
        print(f'-- {employee_id}')