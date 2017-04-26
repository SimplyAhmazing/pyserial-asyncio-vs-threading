# Asyncio pySerial vs Thread pySerial

Run 1
```
python test_asyncio.py > a1.txt  0.33s user 0.14s system 3% cpu 14.234 total
python test_threading.py > t1.txt  0.12s user 0.12s system 3% cpu 7.264 total
```

Run 2
```
python test_asyncio.py > a1.txt  0.33s user 0.16s system 3% cpu 14.291 total
python test_threading.py > t2.txt  0.12s user 0.12s system 3% cpu 7.254 total
```

## Asyncio w/uvloop
Run 1:
```
time python test_asyncio.py > a3.txt  0.28s user 0.17s system 3% cpu 14.605 total
```

Run 2:
```
time python test_asyncio.py > a3.txt  0.28s user 0.16s system 3% cpu 14.562 total
```


## Asyncio w/uvloop && safe_read timeout=.02
```
python test_asyncio.py > a4.txt  0.56s user 0.27s system 7% cpu 11.181 total
```

## Asyncio w/uvloop && safe_read timeout=.2
```
python test_asyncio.py > a4.txt  0.27s user 0.19s system 4% cpu 11.329 total
```
