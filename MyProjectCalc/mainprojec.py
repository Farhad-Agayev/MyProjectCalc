name = ""
surname = ""
age = 0
grades = []

while True:
    print('\n-----Калькулятор для оценивания студента-------')
    print('1.   Ввести данные студента')
    print('2.   Добавить оценку')
    print('3.   Показать все оценки')
    print('4.   Рассчитать итоговый результат')
    print('5.   Выход')

    choice = input('Выберите действие от 1 - го до 5-ти : ').strip()

    if choice == "1":
        name = input("Введите Имя: ")
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))

        if name == "" or  surname == "" or age <5 or age >100:
            print("Заполните поля верно!")



        else:
            grades = []
            print('Вы успешно зарегестрировалист  как студент!')

    elif choice == "2":
        grade = int(input('Введите оценку (от 0 до 100): '))
        if grade >0 and grade <100:
            grades.append(grade)
            print('Вы успешно добавили оценку')
        else:
            print("Введите верную оценку!")
    elif choice == "3":
        if grades == 0:
            print("Оценки отсутсвуют")
        print(f"Уважаемый(ая) {name} , вот ваши оценки: {grades}")
    elif choice == "4":
        print('')
    elif choice == "5":
        print("Выход из программы")
        break
    else:
        print("введи число от 1 до 5!"  )