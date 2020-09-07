# CGI

## Apache CGI

Installiamo apache su WSL

```
$ sudo apt-get install apache2
```
È possibile avviare e fermare il server apache con
```
sudo service apache2 start
sudo service apache2 stop
```

La cartella di default dalla quale vengono eseguiti gli scripts CGI è `/usr/lib/cgi-bin `

Per far funzionare CGI `sudo nano /etc/apache2/apache2.conf`

```
<Directory /var/www/cgi-bin/>
    AddHandler cgi-script .cgi .pl
    Options FollowSymLinks ExecCGI
    AllowOverride None
</Directory>
```
`sudo nano /etc/apache2/sites-enabled/000-default.conf`

```
<Files ~ "\.(pl|cgi)$">
    SetHandler perl-script
    PerlResponseHandler ModPerl::PerlRun
    Options +ExecCGI
    PerlSendHeader On
</Files>
```

### Mancanza di Perl su WSL

Se non c'è supporto a perl (siamo su WSL) allora eseguire

```
sudo a2enmod cgi
sudo service apache2 restart
```

## Script CGI

A questo punto Apache servirà gli script sotto la cartella `\usr\lib\cgi-bin` all'indirizzo `http://localhost/cgi-bin/`

> Nota, per Ubuntu 20.04 la cartella completa è `C:\Users\<user>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs\usr\lib\cgi-bin`

## Python CGI

Eseguire il server nel file `serve.py`, oppure eseguendo il comando

```
python3 -m http.server --bind localhost --cgi 9000
```

