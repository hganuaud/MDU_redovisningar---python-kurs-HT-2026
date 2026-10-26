print('TODO MANAGER')
print('_' * 20)
print('list | List todos')
print('add  | Add todo')
print('rm   | Remove')
print('cls  | Exit')
print('_' * 20)

todo = []

while True:
    cmd = input('command >')

    if cmd == 'list':
        for i in todo: 
            print(f'- {i}')
    elif cmd == 'add':
        task = input('Add task:')
        if task in todo:
            continue
        todo.append(task)
    elif cmd == 'rm':
        try:
            task = input('Remove task:')
            todo.remove(task)
        except ValueError:
            print("not in list")
    elif cmd == 'cls':
        break
