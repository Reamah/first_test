def calculator():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    choice = input("Введите номер операции (1-4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        if choice == '1':
            result = num1 + num2
            print("Результат:", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат:", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат:", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Результат:", result)
            else:
                print("Ошибка: деление на ноль")
    else:
        print("Неверный выбор операции")

calculator()