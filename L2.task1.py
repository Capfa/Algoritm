# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю
# о невозможности деления на ноль, если он ввел его в качестве делителя.
def count():
  while True:
    z = input('Введите знак (+,-,*,/) для вычисления, или 0 для завершения программы:')
    if z == '0':
      break
    elif z in ('+','-','*','/'):
      a = float(input('Введите первое число a='))
      b = float(input('Введите второе число b='))
      if z == '+':
       print(f'a + b = {a+b}')
      elif z == '-':
         print(f'a - b = {a - b}')
      elif z == '*':
         print(f'a * b = {a * b}')
      elif z == '/':
        if b != 0:
           print(f'a / b = {a / b}')
        else:
          print('Ошибка. Деление на 0')
    else:
      print('Знак не распознан')
print(count())