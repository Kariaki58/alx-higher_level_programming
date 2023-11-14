### JavaScript - Objects, Scopes and Closures

**Resources**

 - [JavaScript object basics](https://intranet.alxswe.com/rltoken/dsSkBB-Cj0tqUFL8eOZLLQ)
 - [Object-oriented JavaScript](https://intranet.alxswe.com/rltoken/qqgqdyHPzUZkKQ5UMnw2MQ)
 - [Class-ES6](https://intranet.alxswe.com/rltoken/NEm-UViCThD5hfq_3Lj9Hg)
 - [Super-ES6](https://intranet.alxswe.com/rltoken/_cxdVKsdqPWbbp2cHtQSbQ)
 - [extends-ES6](https://intranet.alxswe.com/rltoken/6wdl6Bc5yjBplpiZKmr6Zw)
 - [Object prototypes](https://intranet.alxswe.com/rltoken/NiBbDiOlfhfUf4eIigglIw)
 - [Object prototypes](https://intranet.alxswe.com/rltoken/qqgqdyHPzUZkKQ5UMnw2MQ)
 - [Inheritance in JavaScript](https://intranet.alxswe.com/rltoken/qqgqdyHPzUZkKQ5UMnw2MQ)
 - [Closures](https://intranet.alxswe.com/rltoken/CybTMKEDNdTdU99kx_OXgQ)
 - [this/self](https://intranet.alxswe.com/rltoken/XcOkisoKPud4faDDkLMABw)

### How to Run the Scripts

```
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 

guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$

guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$

guillaume@ubuntu:~/0x13$ cat fileA
C is fun!
guillaume@ubuntu:~/0x13$ cat fileB
Python is Cool!!!
guillaume@ubuntu:~/0x13$ ./102-concat.js fileA fileB fileC
guillaume@ubuntu:~/0x13$ cat fileC
C is fun!
Python is Cool!!!
guillaume@ubuntu:~/0x13$  
```
