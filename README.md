port check
python






portチェック

----

単一ポート


```

$ ./main.py -t localhost -p [port number] -t [target host]

```

```

[*] target:localhost port: [port number] [OPEN/CLOSE]

```

------

list形式

```

$ ./main.py -c list -t [target host]

```

```

***********************************
         [*]target : [target host]       
***********************************
[*] port: 000/TCP OPEN
[*] port: 000/TCP OPEN
...




[*] port: 000/TCP OPEN
Done

```
