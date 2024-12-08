print('Задание №2')
holiday = input('Праздник (1 или 0): ')
temperature = input('Градусов на улице: ')
age = input('Возраст: ')
temperature_limit = -27
age_limit = 9
if holiday == 1:
    print('\nИдем к друзьям')
elif int(temperature) > temperature_limit:
    print('\nВ школу :(')
elif int(age) < age_limit:
    print('\nСидим дома :)')
else:
    print('\nТащимся в школу :(')
