print('{0:14} | {1:12}'.format('Vegetable Name', 'Quantity Pcs'))
print('{0:14} | {1:12}'.format('Asparagus', 3))
print('{0:14} | {1:12}'.format('Onions', 1234))

print("########################################################")
print('{0:14} | {1:<12}'.format('Vegetable Name', 'Quantity Pcs'))
print('{0:14} | {1:<12}'.format('Asparagus', 3))
print('{0:14} | {1:<12}'.format('Onions', 1234))

print("########################################################")
print('{0:>14} | {1:<12}'.format('Vegetable Name', 'Quantity Pcs'))
print('{0:>14} | {1:<12}'.format('Asparagus', 3))
print('{0:>14} | {1:<12}'.format('Onions', 1234))

print("########################################################")
print('{0:8} | {1:<8}'.format('Vegetable', 'Quantity'))
print('{0:9} | {1:<8.2f}'.format('Asparagus', 2.33333))
print('{0:9} | {1:<8.2f}'.format('Onions', 10))

print("########################################################")
print('{0:8} | {1:>8}'.format('Vegetable', 'Quantity'))
print('{0:9} | {1:>8.3f}'.format('Asparagus', 2.8947))
print('{0:9} | {1:>8.2f}'.format('Onions', 10))


persons=2
cost=102
print('There are {0} persons who got {1} Rupees each and In total they have ' f"{1}*{1}".format(persons,cost))