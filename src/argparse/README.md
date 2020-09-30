# Argparse CLI

Code for build a command-line interface using argparse module.

Features:
1. Commands (bull, bear)
2. Arguments (name)
3. Options/Flags (--greeting=<str>, --caps)
4. Version Printing (--version)
5. Automated Help Messages

Checking funcionality
```
$ python3 cli.py bull market
bull, market!

$ python3 cli.py bear --caps market
BEAR, MARKET!

$ python3 cli.py bear --greeting=none --caps money 
NONE, MONEY!
```

Checking version
```
$ python3 cli.py --version
1.0.0
```

Checking help
```
$ python3 cli.py --help
usage: cli.py [-h] [--version] {bull,bear} ...

positional arguments:
  {bull,bear}

optional arguments:
  -h, --help   show this help message and exit
  --version    show program's version number and exit
```