tasks = []

print('=================')
print('UNT TRACKER')
print('=================')

print('1. Добавить задачу')
print('2. Посмотреть задачи')
print('3. Удалить задачу')
print('4. Выполнить задачу')
print('5. Выйти')

while True:
    choose_action = int(input('Выберите действие: '))

    if choose_action == 1:
        task_name = input('Введите задачу: ')
        tasks.append(task_name)
        print(tasks)
        print('Задача добавлена')

    elif choose_action == 2:
        print('Ваши задачи:')
        for task in tasks: 
            print(task)

    elif choose_action == 3:
        print