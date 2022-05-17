# Поработайте с переменными,
# создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

n = input('Enter you name:')
print(f'name = {n}')

i = int(input("Enter int number:"))
print(f"int = {i}")

fl = float(input("Enter float number:"))
print(f"float = {fl}")

a, b = map(int, input("input a b:").split())
print(a)
print(b)
print("{:5d}".format(a))

data = input("Enter array of numbers (with space):")
s = data.split()
print(s)
