# **Лабораторна робота №2**

---

## Необхідні ресурси:

- Встановлений компілятор для Python.

## Інформація про програму:

- Виводить в терміналі "Hello World!".
- Виконує команди: ping, echo, login, list, msg, file, exit.

## Опис Команд:

### 1. Команда `ping <Address: String>`. Пінгує задану адресу.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: ping 192.168.1.1
Entered command = "ping", command parameter = ['192.168.1.1']
//////////////////////////////////////////////////

Result:
pinging 192.168.1.1 ...
ping 192.168.1.1 request success.
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: ping 192.168.1.2 192.145.1.1
Entered command = "ping", command parameter = ['192.168.1.2', '192.145.1.1']
//////////////////////////////////////////////////

Result:
PING ERROR | BAD REQUEST
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 2. Команда `echo <anyText: String> <anyText: String> ...`. Виводить вказаний текст.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: echo Hello World!
Entered command = "echo", command parameter = ['Hello', 'World!']
//////////////////////////////////////////////////

Result:
Hello
World!
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: echo "Hello World!"
Entered command = "echo", command parameter = ['Hello World!']
//////////////////////////////////////////////////

Result:
Hello World!
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 3. Команда `login <login: String> <password: String>`. Здійснює вхід та перевірку на існування користувача.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: login pavlo pass1
Entered command = "login", command parameter = ['pavlo', 'pass1']
//////////////////////////////////////////////////

Result:
LOGIN SUCCESS:
 Hello, Pavlo
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: login Vasya 111
Entered command = "login", command parameter = ['Vasya', '111']
//////////////////////////////////////////////////

Result:
INCORRECT CREDENTIALS
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: login Vasya
Entered command = "login", command parameter = ['Vasya']
//////////////////////////////////////////////////

Result:
INCORRECT INPUT
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 4. Команда `list`. Виводить вмена всіх користувачів.

#### База даних:

- names = `['Pavlo', 'Iryna', 'Vasyl', 'Orest', 'Mykhailo']`
- logins = `['pavlo', 'iryna', 'vasyl', 'orest', 'mykhailo']`
- passwords = `['pass1', 'pass2', 'pass3', 'pass4', 'pass5']`

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: list
Entered command = "list", command parameter = []
//////////////////////////////////////////////////

Result:
1. Pavlo
2. Iryna
3. Vasyl
4. Orest
5. Mykhailo
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 5. Команда `msg <destinationUser: String> <text: String>`. Надсилає повідомлення до існуючого користувача.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: msg Vasyl Hello
Entered command = "msg", command parameter = ['Vasyl', 'Hello']
//////////////////////////////////////////////////

Result:
MESSAGE SENDED
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: msg Oleg Hello
Entered command = "msg", command parameter = ['Oleg', 'Hello']
//////////////////////////////////////////////////

Result:
USER NOT FOUND
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: msg Orest
Entered command = "msg", command parameter = ['Orest']
//////////////////////////////////////////////////

Result:
INCORRECT INPUT
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 6. Команда `file <destinationUser: String> <filename: String>`. Надсилає вказаний файл.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: file Pavlo README.md
Entered command = "file", command parameter = ['Pavlo', 'README.md']
//////////////////////////////////////////////////

Result:
FILE SENDED
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: file Pavlo msg.json
Entered command = "file", command parameter = ['Pavlo', 'msg.json']

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: file Oleg file.exe
Entered command = "file", command parameter = ['Oleg', 'file.exe']
//////////////////////////////////////////////////

Result:
USER NOT FOUND
falcon@Makohons-MBP Distributed_systems_NULP %

//////////////////////////////////////////////////

falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: file hello
Entered command = "file", command parameter = ['hello']
//////////////////////////////////////////////////

Result:
INCORRECT INPUT
falcon@Makohons-MBP Distributed_systems_NULP %
```

### 7. Команда `exit`. Виходить з програми.

### Виконання:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: exit
Entered command = "exit", command parameter = []
//////////////////////////////////////////////////

Result:
LOGGED OUT
falcon@Makohons-MBP Distributed_systems_NULP %
```

### Виконання програми при введенні неправильної команди:

```text
falcon@Makohons-MBP Distributed_systems_NULP % python3 l2.py
Hello World!
Type your command: gg
Entered command = "gg", command parameter = []
//////////////////////////////////////////////////

Result:
COMMAND NOT FOUND
falcon@Makohons-MBP Distributed_systems_NULP %
```
