print("Hello World!")
names = ['Pavlo', 'Iryna', 'Vasyl', 'Orest', 'Mykhailo']
logins = ['pavlo', 'iryna', 'vasyl', 'orest', 'mykhailo']
passwords = ['pass1', 'pass2', 'pass3', 'pass4', 'pass5']


def Commands(command):
    allowSpace = 0
    commandCounter = 0
    commandType = ""
    commandParam = []
    collector = ""
    for char in command:
        if (char == "'") | (char == '"'):
            allowSpace = 1 - allowSpace
        elif (char == ' ') & (commandCounter == 0):
            commandType = collector
            collector = ""
            commandCounter = commandCounter + 1
        elif (char == ' ') & (commandCounter > 0) & (allowSpace == 0):
            commandCounter = commandCounter + 1
            commandParam.append(collector)
            collector = ""
        else:
            collector = collector + char
    if commandCounter == 0:
        commandType = collector
        collector = ""
    elif commandCounter > 0:
        commandParam.append(collector)
        collector = ""

    print('Entered command = "' + commandType +
          '", ' + "command parameter =", commandParam)

    if commandType == "ping":
        if len(commandParam) == 1:
            collector = "pinging " + commandParam[0] + " ...\n"
            collector = collector + "ping " + \
                commandParam[0] + " request success."
            return collector
        else:
            return "PING ERROR | BAD REQUEST"
    elif commandType == "echo":
        collector = ""
        for i in range(len(commandParam)):
            collector = collector + commandParam[i]
            if (i + 1) != len(commandParam):
                collector = collector + "\n"
        return collector
    elif commandType == "login":
        if len(commandParam) == 2:
            user_number = -1
            for i in range(len(logins)):
                if logins[i] == commandParam[0]:
                    user_number = i
                    break
            if user_number > -1:
                if passwords[i] == commandParam[1]:
                    return "LOGIN SUCCESS:\n Hello, " + names[user_number]
                else:
                    return "INCORRECT CREDENTIALS"
            else:
                return "INCORRECT CREDENTIALS"
        else:
            return "INCORRECT INPUT"
    elif commandType == "list":
        collector = ""
        for i in range(len(names)):
            collector = collector + str(i+1) + ". " + names[i]
            if (i + 1) != len(names):
                collector = collector + "\n"
        return collector
    elif commandType == "msg":
        if len(commandParam) == 2:
            if commandParam[0] in names:
                return "MESSAGE SENDED"
            else:
                return "USER NOT FOUND"
        else:
            return "INCORRECT INPUT"
    elif commandType == "file":
        if len(commandParam) == 2:
            if commandParam[0] in names:
                try:
                    f = open(commandParam[1])
                    f.close()
                except FileNotFoundError:
                    return "FILE NOT FOUND"
                return "FILE SENDED"
            else:
                return "USER NOT FOUND"
        else:
            return "INCORRECT INPUT"
    elif commandType == "exit":
        return "LOGGED OUT"
    else:
        return "COMMAND NOT FOUND"


inputedCommand = input("Type your command: ")
outputTerminal = Commands(inputedCommand)
print("/ "*50)
print("\nResult:")
print(outputTerminal)
