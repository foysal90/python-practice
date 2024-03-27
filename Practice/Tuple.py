items = ('Crispy Chicken', 'Tandoori', 'Chilli chicken')
# checking ranges
print('Ranges: ', items[1:3])

# update
cd = list(items)
cd.append('Butter Chicken')
cd[2] = 'CTM'
btp = tuple(cd)
print(btp)