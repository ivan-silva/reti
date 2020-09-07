# Telnet

Prova di esecuzione dei comandi per effettuare chiamate HTTP dopo essersi connessi con `telnet netlab.fis.unipr.it 80`.

### GET

```
GET /test.txt HTTP/1.0

HTTP/1.1 200 OK
Date: Mon, 07 Sep 2020 21:08:17 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
ETag: "11-59b7ae27c33d3"
Accept-Ranges: bytes
Content-Length: 17
Connection: close
Content-Type: text/plain; charset=UTF-8

pagina di prova
```

```
GET /test.txt HTTP/1.1
host: netlab.fis.unipr.it

HTTP/1.1 200 OK
Date: Mon, 07 Sep 2020 21:14:20 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
ETag: "11-59b7ae27c33d3"
Accept-Ranges: bytes
Content-Length: 17
Content-Type: text/plain; charset=UTF-8

pagina di prova


```

```
GET /test.txt HTTP/1.0
Connection: Keep-Alive

HTTP/1.1 200 OK
Date: Mon, 07 Sep 2020 21:13:43 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
ETag: "11-59b7ae27c33d3"
Accept-Ranges: bytes
Content-Length: 17
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/plain; charset=UTF-8

pagina di prova
```

```
GET /test.txt HTTP/1.1
host: netlab.fis.unipr.it
Connection: close

HTTP/1.1 200 OK
Date: Mon, 07 Sep 2020 21:15:38 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
ETag: "11-59b7ae27c33d3"
Accept-Ranges: bytes
Content-Length: 17
Connection: close
Content-Type: text/plain; charset=UTF-8

pagina di prova

```



#### If-Modified-Since

```
GET /test.txt HTTP/1.0
If-Modified-Since: Mon, 06 Jan 2020 17:00:00 GMT

HTTP/1.1 304 Not Modified
Date: Mon, 07 Sep 2020 21:12:31 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Connection: close
ETag: "11-59b7ae27c33d3"

```

### HEAD

```
HEAD /test.txt HTTP/1.0

HTTP/1.1 200 OK
Date: Mon, 07 Sep 2020 21:10:48 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
ETag: "11-59b7ae27c33d3"
Accept-Ranges: bytes
Content-Length: 17
Connection: close
Content-Type: text/plain; charset=UTF-8

```

### Connessione tramite proxy

```
174931@vdi-lgnlnx-01:~$ telnet proxy.unipr.it 8080
Trying 160.78.50.212...
Connected to srv-proxyweb-01.unipr.it.
Escape character is '^]'.
GET http://netlab.fis.unipr.it/test.txt  HTTP/1.0

HTTP/1.1 200 OK
Last-Modified: Mon, 06 Jan 2020 16:09:31 GMT
Accept-Ranges: bytes
Content-Length: 17
Content-Type: text/plain; charset=UTF-8
Date: Mon, 07 Sep 2020 21:16:31 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/5.4.45
ETag: "11-59b7ae27c33d3"
Age: 2
X-Cache: HIT from proxy.unipr.it
X-Cache-Lookup: HIT from proxy.unipr.it:8080
Via: 1.1 simon.cce.unipr.it (squid/3.5.20)
Connection: close

pagina di prova

```

