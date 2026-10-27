tasks = []
done_tasks = []

print('=================')
print('UNT TRACKER')
print('=================')

while True:
    print('1. Добавить задачу')
    print('2. Посмотреть задачи')
    print('3. Удалить задачу')
    print('4. Выполнить задачу')
    print('5. Выйти')


    choose_action = int(input('Выберите действие: '))

    if choose_action == 1:
        task_name = input('Введите задачу: ')
        tasks.append(task_name)
        print('Задача добавлена')

    elif choose_action == 2:
        print('Активные задачи: ')
        for task in tasks: 
            print(task)
        print('Выполненные задачи: ')
        for j in done_tasks:
            print(j)

    elif choose_action == 3:
        for i, task in enumerate(tasks):
            print(i + 1, '.', task, sep="")
        number = int(input('Номер задачи для удаления: '))
        tasks.pop(number-1)
        print('Задача удалена')

    elif choose_action == 4:
        for n, task in enumerate(tasks):
            print(n + 1, '.', task, sep="")
        number = int(input('Номер выполненной задачи: '))
        done_tasks.append(tasks.pop(number - 1))
        print('Задача выполнена')

    elif choose_action == 5:
        break