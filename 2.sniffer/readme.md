## tcpdump

**Cattura dei pacchetti con tcpdump o tshark (a linea di comando)**

Ho utilizzato la versione per windows di tcpdump, https://www.microolap.com/products/network/tcpdump/

Per ottenere gli adattatori

```

.\tcpdump.exe -D
1.\Device\{F2E5018C-8A94-40E3-B569-D6718D3BDD90} (Microsoft Wi-Fi Direct Virtual Adapter)
2.\Device\{8A6424E6-2631-4D8D-8A0D-FED2C4F208C2} (Fortinet SSL VPN Virtual Ethernet Adapter)
3.\Device\{9D5E5DD6-77B0-4CBA-A607-4D4F8651C148} (Realtek PCIe GBE Family Controller)
4.\Device\{21D97A7F-0488-40E1-925D-E67CDD02C569} (Intel(R) Dual Band Wireless-AC 7265)
5.\Device\{87BA5C73-56D1-477C-AED3-1B50E6EED602} (Microsoft Wi-Fi Direct Virtual Adapter)
6.\Device\{251C6183-844B-4746-A773-6961D4577A0F} (WAN Miniport (Network Monitor))
7.\Device\{489FAA19-A9B9-4027-9A60-3561D3643947} (TAP-Windows Adapter V9)
8.\Device\{D676DE5E-B336-4F32-B6BD-30C0B24CA9D6} (Microsoft KM-TEST Loopback Adapter)
9.\Device\{C7636869-35FD-4499-9308-73E15E250EE5} (VirtualBox Host-Only Ethernet Adapter)
```

Per mettersi in ascolto

```
 .\tcpdump.exe -i 4 port 80 -w esercizio2_tcpdump.pcap
```

Questo però non ha dato il risultato aspettato e non è riuscito a leggere correttamente i pacchetti, ho sostituito questa parte con tshark(opzionale).

## tshark

Installando wireshark si ha a disposizione anche tshark

```
C:\"Program Files"\Wireshark/tshark -i 5 -w httpsnif.pcap port 80
```

Si ottiene una 301 redirect su https ma per lo scopo dell'esercitazione possiamo concludere  di aver intercettato i pacchetti correttamente

```
GET /rfc/rfc1958.txt HTTP/1.1
User-Agent: Wget/1.20.3 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: tools.ietf.org
Connection: Keep-Alive
Date: Mon, 07 Sep 2020 16:14:39 GMT
Server: Apache/2.2.22 (Debian)
Location: https://tools.ietf.org/rfc/rfc1958.txt
Vary: Accept-Encoding
Content-Length: 326
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="https://tools.ietf.org/rfc/rfc1958.txt">here</a>.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at tools.ietf.org Port 80</address>
</body></html>
```

