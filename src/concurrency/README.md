# concurrency

Code for playing with concurrency.

Features:
- Speed Up an I/O-Bound Program
    - Pre-emptive multitasking (threading)
    - Cooperative multitasking (asyncio)
    - Multiprocessing (multiprocessing)
- Speed Up a CPU-Bound Program
    - Pre-emptive multitasking (threading)
    - Multiprocessing (multiprocessing)
 
### I/O-Bound Program
Checking funcionality
```
$ python3 iosync.py
Downloaded 160 in 23.065617322921753 seconds

$ python3 iothread.py
Downloaded 160 in 3.683701992034912 seconds

$ python3 ioasync.py
Downloaded 160 in 2.3265864849090576 seconds

$ python3 iomultipro.py
Downloaded 160 in 3.0351479053497314 seconds
```

### CPU-Bound Program
Checking funcionality
```
$ python3 cpusync.py 
Duration 6.71713662147522 seconds

$ python3 cputhread.py 
Duration 7.3348870277404785 seconds

$ python3 cpumultipro.py 
Duration 1.917677879333496 seconds
```
