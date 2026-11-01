all_students = [
    'Anna',
    'Lars',
    'Eva',
    'Mikael',
    'Maria',
    'Anders'
]

team_a = [
    'Anna',
    'Maria'
]

team_b = [
    'Eva',
    'Anders'
]

for student in all_students:
    if student in team_a or student in team_b:
        continue 
    else: 
        print(student)

