# Nettools

Scelgo https://www.mit.edu/

## Traceroute

Arrivo fino alla rete akamai, poi i traceroute vengono ignorati

```
174931@vdi-lgnlnx-01:~$ traceroute www.mit.edu
traceroute to www.mit.edu (104.83.115.155), 30 hops max, 60 byte packets
 1  _gateway (160.78.51.254)  0.210 ms  0.195 ms  0.204 ms
 2  160.78.254.100 (160.78.254.100)  1.006 ms  1.583 ms  1.165 ms
 3  160.78.254.254 (160.78.254.254)  0.373 ms  0.371 ms  0.355 ms
 4  160.78.253.100 (160.78.253.100)  1.165 ms  1.234 ms  1.837 ms
 5  ru-uni-parma-rettorato-rx1-bo3.bo3.garr.net (193.206.128.221)  3.502 ms  3.502
 6  rx1-bo3-rx2-mi1.mi1.garr.net (90.147.81.221)  8.698 ms  8.709 ms  8.758 ms
 7  rx2-mi1-rx2-mi2.mi2.garr.net (90.147.80.10)  10.138 ms  10.106 ms  6.888 ms
 8  mno-b2-link.telia.net (80.239.135.52)  7.982 ms  8.878 ms  7.926 ms
 9  akamai-ic-338595-mno-b2.c.telia.net (213.248.103.26)  7.320 ms  8.653 ms  7.37
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *

```

## Ping

Il ping con route è evidentemente ignorato dai router in gioco

```
174931@vdi-lgnlnx-01:~$ ping -c 1  -R  www.mit.edu
PING e9566.dscb.akamaiedge.net (104.83.115.155) 56(124) bytes of data.

--- e9566.dscb.akamaiedge.net ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms
```

## Dig

Dig mostra i `CNAME` della rete akamaiedge e l'indirizzo effettivo di collegamento. Non è presente idirizzo ipv6

```

; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> www.mit.edu
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42523
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;www.mit.edu.                   IN      A

;; ANSWER SECTION:
www.mit.edu.            1073    IN      CNAME   www.mit.edu.edgekey.net.
www.mit.edu.edgekey.net. 8      IN      CNAME   e9566.dscb.akamaiedge.net.
e9566.dscb.akamaiedge.net. 13   IN      A       104.83.115.155

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Mon Sep 07 18:51:10 CEST 2020
;; MSG SIZE  rcvd: 129

```

## Whois

```
174931@vdi-lgnlnx-01:~$ whois mit.edu
This Registry database contains ONLY .EDU domains.
The data in the EDUCAUSE Whois database is provided
by EDUCAUSE for information purposes in order to
assist in the process of obtaining information about
or related to .edu domain registration records.

The EDUCAUSE Whois database is authoritative for the
.EDU domain.

A Web interface for the .EDU EDUCAUSE Whois Server is
available at: http://whois.educause.edu

By submitting a Whois query, you agree that this information
will not be used to allow, enable, or otherwise support
the transmission of unsolicited commercial advertising or
solicitations via e-mail.  The use of electronic processes to
harvest information from this server is generally prohibited
except as reasonably necessary to register or modify .edu
domain names.

-------------------------------------------------------------

Domain Name: MIT.EDU

Registrant:
        Massachusetts Institute of Technology
        77 Massachusetts Ave
        Cambridge, MA 02139
        US

Administrative Contact:
        Mark Silis
        Massachusetts Institute of Technology
        MIT Room W92-167, 77 Massachusetts Avenue
        Cambridge, MA 02139-4307
        US
        +1.6173245900
        mark@mit.edu

Technical Contact:
        MIT Network Operations
        Massachusetts Institute of Technology
        MIT Room W92-167, 77 Massachusetts Avenue
        Cambridge, MA 02139-4307
        US
        +1.6172538400
        noc@mit.edu

Name Servers:
        EUR5.AKAM.NET
        USW2.AKAM.NET
        ASIA1.AKAM.NET
        USE5.AKAM.NET
        USE2.AKAM.NET
        ASIA2.AKAM.NET
        NS1-173.AKAM.NET
        NS1-37.AKAM.NET

Domain record activated:    23-May-1985
Domain record last updated: 23-Jan-2019
Domain expires:             31-Jul-2021

```

## Wget

```
174931@vdi-lgnlnx-01:~$ wget https://ocw.mit.edu/courses/mathematics/18-785-number-theory-i-fall-2019/lecture-notes/MIT18_785F19_full_notes.pdf
--2020-09-07 18:59:55--  https://ocw.mit.edu/courses/mathematics/18-785-number-theory-i-fall-2019/lecture-notes/MIT18_785F19_full_notes.pdf
Risoluzione di ocw.mit.edu (ocw.mit.edu)... 151.101.242.133
Connessione a ocw.mit.edu (ocw.mit.edu)|151.101.242.133|:443... connesso.
Richiesta HTTP inviata, in attesa di risposta... 200 OK
Lunghezza: 8760256 (8,4M) [application/pdf]
Salvataggio in: "MIT18_785F19_full_notes.pdf"

MIT18_785F19_full_no 100%[====================>]   8,35M  41,2MB/s    in 0,2s

2020-09-07 18:59:56 (41,2 MB/s) - "MIT18_785F19_full_notes.pdf" salvato [8760256/8760256]

```

