name = ""
surname = ""
age = 0
grades = []

while True:
    print('\n-----  \033[34mКалькулятор для оценивания студента\033[0m  -------')
    print('1.   Ввести данные студента')
    print('2.   Добавить оценку')
    print('3.   Показать все оценки')
    print('4.   Рассчитать итоговый результат')
    print('5.   Выход')

    choice = input('Выберите действие от 1 - го до 5-ти : ').strip()

    if choice == "1":
        name = input("\033[35mВведите Имя:\033[0m ").title()
        surname = input('\033[35mВведите фамилию:\033[0m ').title()
        age = int(input('\033[35mВведите возраст:\033[0m '))

        if name == "" or  surname == "" or age <5 or age >100:
            print("Заполните поля верно!")



        else:
            grades = []
            print('Вы успешно зарегестрировалист  как студент!')

    elif choice == "2":
        if name == "" or  surname == "" or age <5 or age >100:
            print("Сначала заполните данные верно!")
        grade = int(input('Введите оценку (от 0 до 100): '))
        if grade >0 and grade <100:
            grades.append(grade)
            print('Вы успешно добавили оценку')
        else:
            print("Введите верную оценку!")
    elif choice == "3":

        if grades == []:
            print("Оценки отсутсвуют")
        print(f"Уважаемый(ая) {name} , вот ваши оценки:{grades}")


    elif choice == "4":
        if name == "" or  surname == "" or age <5 or age >100:
            print("Сначала заполните данные верно!")
        sred_ar = sum(grades) / len(grades)

        print(' ФИO: ', name , surname,)
        print(" Возраст: ", age)
        print(" Cписок оценок:" ,grades)
        print(" Колличество оценок: ", len(grades))
        print(' Cредний балл:' , sred_ar)
        print(' Mаксимальная оценка:' , max(grades))
        print(" Минимальная оценка:" , min(grades))
        if 90<= sred_ar <=100:
            print('отлично')
        elif 80<= sred_ar <= 89.99:
            print("Хорошо")
        elif 70<= sred_ar <= 79.99:
            print('Удовлетворительно')
        elif 60<= sred_ar <=69.99:
            print('Слабо')
        else:
            print("Неудовлетворительно")






    elif choice == "5":
        print("\033[31mВыход из программы\033[0m")
        break
    else:
        print("введи число от 1 до 5!"  )