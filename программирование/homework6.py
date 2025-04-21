my_dict = {'Artem': 2009, 'Anton': 2005, 'Roma': 2015}
print(my_dict)
print(my_dict['Artem'])
print(my_dict.get('Yan', "Такого ключа нет"))
my_dict.update({'Sasha': 2010,
                'Roma': 2015})
print(my_dict)
del my_dict['Anton']
print(my_dict)

my_set = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(my_set)
my_set.add(4)
my_set.add(5)
print(my_set)
my_set.remove(1)
print(my_set)