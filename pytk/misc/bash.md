# Bash Notes

## Zip Directory

```
sudo apt-get install zip
zip -r compressed_filename.zip foldername
```

## Encrypt & Decrypt File

Encrypt: `openssl aes-256-cbc -in FILE.txt -out ENCRYTED_FILE.enc`

Decrypt: `openssl aes-256-cbc -d -in ENCRYTED_FILE.enc -out FILE.txt`


## Find process using port

`sudo netstat -nlp | grep :8080`
