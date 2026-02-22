PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

nice_price_list = PRICE_LIST.splitlines()

data = [(item.split()[0], item.split()[1][:-1]) for item in nice_price_list]

new_dict = {key: int(value) for key, value in data}
print(new_dict)
