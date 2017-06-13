# Notes

## Installation and Dependencies

```
gunicorn --bind 0.0.0.0:5000 wsgi:app
#
sudo vim /etc/systemd/system/coherence.service
#
sudo vim /etc/nginx/sites-available/coherence
#
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/coherence /etc/nginx/sites-enabled
```

## Script
```
sudo systemctl disable coherence
sudo systemctl stop coherence
sudo systemctl start coherence
sudo systemctl enable coherence
sudo nginx -t
sudo systemctl restart nginx
```
