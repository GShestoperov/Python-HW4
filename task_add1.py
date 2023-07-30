# задача 1 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции


# преобразование системы счисления с двоичной по 10-ной (base = 2..10)
def covertNotation(num: int, base: int) -> str:
    res = ""

    if base < 2 or base > 10:
        return ""

    quotient = 1
    while quotient > 0:
        quotient = num // base
        remainder = num % base
        res = str(remainder) + res
        num = quotient

    return res


num: int = int(input("Введите число: "))
resOct: str = "0o" + covertNotation(num, 8)
resOctCheck: str = oct(num)
if resOctCheck == resOct:
    print(f"Число переведено в 8-ую систему счисления: {resOct}")
else:
    print("Ошибка при переводе в 8-ую систему счисления")

resBin: str = "0b" + covertNotation(num, 2)
resBinCheck = bin(num)
if resBinCheck == resBin:
    print(f"Число переведено в 2-ую систему счисления: {resBin}")
else:
    print("Ошибка при переводе в 2-ую систему счисления")
