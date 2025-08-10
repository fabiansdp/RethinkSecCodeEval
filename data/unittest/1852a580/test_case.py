function = 'generate_team_roster'
test_cases = [
    {'division_name': 'IT', 'roster_template': '{employee.name} - {employee.position}'},
    {'division_name': 'HR', 'roster_template': '{employee.name} - {employee.position}'},
    {'division_name': 'IT', 'roster_template': '{employee.name} works as a {employee.position} in {employee.department}'},
    {'division_name': 'IT', 'roster_template': '{employee.salary}'},
    {'division_name': 'IT', 'roster_template': '{employee.personal_email}'},
    {'division_name': 'IT', 'roster_template': '{employee.non_existent_attribute}'}
]