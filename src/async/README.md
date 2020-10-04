# async

Code for understanding asynchronous programming.

Features:
- Synchronous Programming
- Simple Cooperative Concurrency
- Cooperative Concurrency With Blocking Calls
- Cooperative Concurrency With Non-Blocking Calls
- Synchronous (Blocking) HTTP Calls
- Asynchronous (Non-Blocking) HTTP Calls
 
### Synchronous Programming
Checking funcionality
```
$ python3 sync.py 
Task One running
Task One total: 15
Task One running
Task One total: 10
Task One running
Task One total: 5
Task One running
Task One total: 2
Task Two nothing to do
```

### Simple Cooperative Concurrency
Checking funcionality
```
$ python3 cooperative.py 
Task One running
Task Two running
Task Two total: 10
Task Two running
Task One total: 15
Task One running
Task Two total: 5
Task One total: 2
```

### Cooperative Concurrency With Blocking Calls
Checking funcionality
```
$ python3 cooperativeblock.py 
Task One running
Task One elapsed time: 15.0
Task Two running
Task Two elapsed time: 10.0
Task One running
Task One elapsed time: 5.0
Task Two running
Task Two elapsed time: 2.0

Total elapsed time: 32.0
```

### Cooperative Concurrency With Non-Blocking Calls
Checking funcionality
```
$ python3 cooperativenonblock.py 
Task One running
Task Two running
Task Two total elapsed time: 10.0
Task Two running
Task One total elapsed time: 15.0
Task One running
Task Two total elapsed time: 5.0
Task One total elapsed time: 2.0

Total elapsed time: 17.0
```

### Synchronous (Blocking) HTTP Calls
Checking funcionality
```
$ python3 synchttpcall.py 
Task One getting URL: http://google.com
Task One elapsed time: 0.3
Task Two getting URL: http://yahoo.com
Task Two elapsed time: 3.1
Task One getting URL: http://linkedin.com
Task One elapsed time: 0.9
Task Two getting URL: http://apple.com
Task Two elapsed time: 0.6
Task One getting URL: http://microsoft.com
Task One elapsed time: 1.5
Task Two getting URL: http://facebook.com
Task Two elapsed time: 0.9
Task One getting URL: http://twitter.com
Task One elapsed time: 1.4

Total elapsed time: 8.6
```

### Asynchronous (Non-Blocking) HTTP Calls
Checking funcionality
```
$ python3 asynchttpcall.py 
Task One getting URL: http://google.com
Task Two getting URL: http://yahoo.com
Task One total elapsed time: 0.3
Task One getting URL: http://linkedin.com
Task One total elapsed time: 0.3
Task One getting URL: http://apple.com
Task One total elapsed time: 0.3
Task One getting URL: http://microsoft.com
Task Two total elapsed time: 0.9
Task Two getting URL: http://facebook.com
Task Two total elapsed time: 0.4
Task Two getting URL: http://twitter.com
Task One total elapsed time: 0.5
Task Two total elapsed time: 0.3

Total elapsed time: 1.7
```