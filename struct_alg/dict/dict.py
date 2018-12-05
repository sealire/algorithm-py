dict = {'Name': 'Maxsu', 'Age': 27, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict['Age'] = 28  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']
print("dict['Name']: ", dict['Name'])
