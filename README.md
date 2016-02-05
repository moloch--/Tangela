Tangela
========
![Browser Security Tests](static/images/tangela-md.png "Browser Security Tests")

Tangela is a Python implementation of the [Browser Security Handbook's](http://code.google.com/p/browsersec/) security test cases. It can be used to test browsers for various security and privacy vulnerabilties; it also includes additional test cases for crashing browsers.


Setup
========

Tangela runs on Python 2 or Python 3:

```
pip install -r requirements.txt
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
./server.py --ssl-keyfile key.pem --ssl-certfile cert.pem
```
