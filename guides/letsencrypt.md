# Notes

## Getting Certificates

* [Source](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)
* Have nginx installed
* Install letsencrypt
  - `sudo apt-get install letsencrypt`
* Add the follwing lines to the file
  - `sudo nano /etc/nginx/sites-available/default`
```
location ~ /.well-known {
    allow all;
}
```
* Check status of nginx
  - `sudo nginx -t`
* Restart nginx
  - `sudo systemctl restart nginx`
* Register domain with CA
  - `sudo letsencrypt certonly -a webroot --webroot-path=/var/www/html -d example.com -d www.example.com`

**IMPORTANT-1**: The output should be the four previously mentioned certificate files. In a moment, you will configure your web server to use `fullchain.pem` as the certificate file, and `privkey.pem` as the certificate key file.

**IMPORTANT-2**: If you have a website hosted on Digitalocean, then make sure that the subdomain is properly mapped.

## Certificate Locations

* `/etc/letsencrypt/archive/your_domain_name`
* `/etc/letsencrypt/live/your_domain_name`

## Generate Strong Diffie-Hellman Group

`sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048`

## Create a Configuration Snippet Pointing to the SSL Key and Certificate

* Snipped file
  - `sudo nano /etc/nginx/snippets/ssl-example.com.conf`
* Add the following lines into the file:
```
ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
```

## Create a Configuration Snippet with Strong Encryption Settings

* Snippet file
  - `sudo nano /etc/nginx/snippets/ssl-params.conf`
* Add the following lines into the file:
```
# from https://cipherli.st/
# and https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_ecdh_curve secp384r1;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
# Disable preloading HSTS for now.  You can use the commented out header line that includes
# the "preload" directive if you understand the implications.
#add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
ssl_dhparam /etc/ssl/certs/dhparam.pem;
```

## Adjust the Nginx Configuration to Use SSL

* Before we go any further, let's back up our current server block file
  - `sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak`

* Edit the file
  - `sudo nano /etc/nginx/sites-available/default`

* Add the following lines are make
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name example.com www.example.com;
    return 301 https://$server_name$request_uri;
}
server {
    # SSL configuration
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    include snippets/ssl-example.com.conf;
    include snippets/ssl-params.conf;
}
```

## Adjust the Firewall and restart Nginx

* Check firewall status
  - `sudo ufw status`
* Add https and https exceptions
  - `sudo ufw allow 'Nginx Full'`


## Enabling the Changes in Nginx

* Make sure that nginx config is ok
  - `sudo nginx -t`
* Restart nginx
  - `sudo systemctl restart nginx`


## Check rating of setup

`https://www.ssllabs.com/ssltest/analyze.html?d=example.com`


## Letsencrypt compatibility with Http to Https Redirection

#### Edit the sites-available file
Edit `/etc/nginx/sites-available/default` or any other site to look like the following:
```
server {
  listen 80;
  server_name example.com www.example.com;
  include /etc/nginx/snippets/letsencrypt-acme-challenge.conf;
  include /etc/nginx/snippets/http-to-https-redirect.conf;
}

server {
  # SSL configuration
  listen 443 ssl;
  server_name example.com www.example.com;

  include /etc/nginx/snippets/ssl-example.com.conf;
  include /etc/nginx/snippets/ssl-params.conf;

  location / {
    include proxy_params;
    # SOME CUSTOM SERVER
    proxy_pass http://127.0.0.1:PORT;
  }
}
```

Where new conf files look like:
* `/etc/nginx/snippets/letsencrypt-acme-challenge.conf`  
```
location ^~ /.well-known/acme-challenge/ {
    default_type "text/plain";
    root         /var/www/html;
}
location = /.well-known/acme-challenge/ {
    return 404;
}
```
* `/etc/nginx/snippets/http-to-https-redirect.conf`  
```
location / {
    return 301 https://$server_name$request_uri;
}
```

#### Update Snippets File
* /etc/nginx/snippets/ssl-example.com.conf
  * Make sure to update this file with the renewed certificate folder path.
