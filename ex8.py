n = int(input('Сколько долек по горизонтали? '))
m = int(input('Сколько долек по вертикали? '))
k = int(input('Сколько долек Вы хотите отломить? '))
if (k < m*n and (k % m == 0 or k % n ==0 )):
     print("yes")
else:
    print("no")