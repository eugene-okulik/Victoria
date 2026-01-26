my_dict = {'tuple': (5, 'text', False, 7.45, 'hello'),
           'list': [7, 'new', 7, True, 8.95],
           'dict': {'key1': 'value1', '2': 21, '5.45': 5.451, 'key4': True, 'key5': 'value5'},
           'set': {'my notes', 8, False, 9.45, 10.15}
           }
print(my_dict['tuple'][-1])

my_dict['list'].append(120)
my_dict['list'].pop(1)
#print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = ('green', 'blue')
#print(my_dict['dict'])
my_dict['dict'].pop('key4')
#print(my_dict['dict'])

my_dict['set'].add('True')
#print(my_dict['set'])
my_dict['set'].pop()
#print(my_dict['set'])

print(my_dict)
