command = ''
status = False
while True:
    command = input('> ')
    if command == 'start':
        if status:
            print('Car already started..!')
        else:
            status = True
            print('Car start..')
    elif command == 'stop':
        if not status:
            print('Car already stopped..!')
        else:
            status = False
            print('Car is stop..')
    elif command == 'quite':
        break
    else:
        print("Can't understand your command")