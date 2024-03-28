items = ('Crispy Chicken', 'Tandoori', 'Chilli chicken')
# checking ranges
print('Ranges: ', items[1:3])

# update
cd = list(items)
# add item
cd.append('Butter Chicken')
# updating
cd[2] = 'CTM'
# remove item
cd.remove('CTM')
btp = tuple(cd)

for x in btp:
    print('Access Items', x)
