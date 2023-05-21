ticket = int(input('Введите 6-значный номер билета '))
if (ticket > 99999 and ticket < 1000000):
    a = ticket % 10
    b = int((ticket / 10)%10)
    c = int((ticket / 100)%10)
    sum1 = a + b + c
    y = ticket // 1000
    a1 = y % 10
    b1 = int((y / 10)%10)
    c1 = int((y / 100)%10)
    sum2 = a1 + b1 + c1
    if sum1 == sum2:
        print ("yes")
    else:
        print ("no")
else: 
    print ("несуществующий номер билета")