name = ""
surname = ""
age = ""
grades = []

while True:
    print('Выберите операцию:')
    print('\t1. Добавить студента')
    print('\t2. Показать всех студентов')
    print('\t3. Найти студента')
    print('\t4. Изменить оценку')
    print('\t5. Удалить студента')
    print('\t6. Средний балл')
    print('\t0. Выход')

    choice = input("Выберите операцию: ")

    if choice == "1":
        name = input("Введите имя студенка: ")
        surname = input("Введите фамилию студенка: ")
        age = int(input('Введите возраст студента: '))
