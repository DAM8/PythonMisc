started = False
cmd = ""

while True:
    cmd = input('enter command: ')
    if cmd == 'start':
        if started == False:
            started =True
            print("car started")
        else:
            print("car is already started")
    elif cmd =='stop':
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stoppped")
    elif cmd=="quit":
        print("game ended")
        break
    else:
        print("cmd not valid")    
            