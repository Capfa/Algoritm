#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
def revers():
  a = int(input('Введите число:'))
  b = 0
  while a> 0:
     b = b*10 + a%10
     a = a//10
  return b

print(revers())