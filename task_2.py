print('Задание №2')
holiday = input('Праздник (1 или 0): ')
temperature = input('Градусов на улице: ')
age = input('Возраст: ')
temperature_limit = -27
age_limit = 9
if holiday == 1:
    print('\nИдем к друзьям')
else:
    print('\nНе идем к друзьям')
if int(temperature) > temperature_limit:
    print('В школу...?')
else:
    print('Не в школу...?')
if int(age) < age_limit:
    print('Сидим дома :)')
else:
    print('Тащимся в школу :(')
