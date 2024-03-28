students = {
    'Name': 'Aisha',
    "Age" :5,
    'City': 'Orlnado',
    "State" : "Florida",
    "ZipCode" : 32836,
    "phone": 12355897894
}
# adding properties
students['Email'] = 'aisha@aisha.com'
print(students)
# updating students
students.update({'Email': 'aisha@gmail.com'})
print(students)
# remove an properties
students.pop('phone')
x = students.get('Name')
print(x)
print(students)
print(students.keys())
print(students.values())

for student in students.values():
    print(student)