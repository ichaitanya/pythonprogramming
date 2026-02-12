command = ''
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('already started')
        else:
            started = True
            print('Car is started....')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car stopped....')
    elif command == 'help':
        print("""
start- to start the car
stop - to stop the car
quite - to quit
        """)
    elif command == 'quit':
        print('its done my guy')
        break
    else:
        print('idk what you talking about :)')

