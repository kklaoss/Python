x = input('x = ')
y = input('y = ')
z = input('z = ')
if int(x) < int(y): x = y
if int(x) < int(z): x = z
print('\nНаибольшее число:', x)
