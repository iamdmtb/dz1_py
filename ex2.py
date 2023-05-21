x = int(input ('Введите трехзначное число: '))
a = x % 10
b = int((x / 10)%10)
c = int((x / 100)%10)
sum = a + b + c
print (sum)