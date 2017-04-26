# Asyncio pySerial vs Thread pySerial

## Reads = 100
```
  python test_asyncio.py > /dev/null  0.25s user 0.15s system 23% cpu 1.706 total
python test_threading.py > /dev/null  0.13s user 0.17s system 19% cpu 1.513 total
```

```
  python test_asyncio.py > /dev/null  0.26s user 0.19s system 23% cpu 1.936 total
python test_threading.py > /dev/null  0.14s user 0.13s system 18% cpu 1.427 total
```

## Reads = 1000
```
  python test_asyncio.py > /dev/null  0.83s user 0.35s system 21% cpu 5.484 total
python test_threading.py > /dev/null  0.42s user 0.27s system 13% cpu 5.122 total
```

```
  python test_asyncio.py > /dev/null  0.72s user 0.31s system 18% cpu 5.476 total
python test_threading.py > /dev/null  0.49s user 0.28s system 14% cpu 5.275 total
```

## Reads=50 & arduino delay=100ms
```
  python test_asyncio.py > /dev/null  0.24s user 0.17s system 6% cpu 6.284 total
python test_threading.py > /dev/null  0.12s user 0.15s system 4% cpu 6.116 total
```
