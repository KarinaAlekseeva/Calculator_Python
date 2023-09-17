import math

print("Добро пожаловать в калькулятор. Выберите операцию из списка: ")

print("|a| Сложить")

print("|b| Вычесть")

print("|c| Умножить")

print("|d| Разделить")

print("|e| Возвести в степень")

print("|f| Извлечь квадратный корень")

print("|g| Вычислить факториал")

print("|h| Вычислить синус")

print("|i| Вычислить косинус")

print("|j| Вычислить тангенс")

print("|k| Выход")

oper = input()

while oper!= "k":
    match oper:
        case "a":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", operand1 + operand2)

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "b":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", operand1 - operand2)

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "c":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", operand1 * operand2)

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")
        
        case "d":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                if operand2 != 0:
                    print("Результат: ", operand1 / operand2)

                    oper = input("Введите операцию: ")
                else:
                    print("На ноль делить нельзя!")

                    oper = input("Введите операцию: ") 
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "e":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите степень, в которую хотите возвести число: "))

                print("Результат: ", operand1 ** operand2)

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "f":
            try:
                operand1 = float(input("Введите первое число: "))
            
                if operand1 >=0:

                    print("Результат: ", math.sqrt(operand1))

                    oper = input("Введите операцию: ") 
                else:
                    print("Не существует корня отрицательного числа")

                    oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "g":
            try:
                factorial = int(input("Введите число: "))  
                if factorial > 0:  
                    for i in range(1, factorial): factorial = factorial * i  
                    print("Результат: ", factorial)  
                elif factorial == 0: 
                    factorial = 1  
                    print("Результат: ", factorial) 
                else:  
                    print("Не существует факториала отрицательного числа!") 
            except(ValueError): 
                print("Введите корректное число")

                oper = input("Введите операцию: ") 
                
        case "h":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", math.sin(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 

        case "i":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", math.cos(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 

        case "j":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", math.tan(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 
                             
        case _:
            print("Данной операции нет в списке")

            oper = input("Введите операцию: ")
            
        