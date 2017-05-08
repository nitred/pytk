## Remote Port Forward + Accept Remote Hosts

#### Configure Remote Host SSHD to accept other remote hosts

The following needs to be done so that the remote host accepts other hosts to connect to remote port forward. This needs to be done on the <remote_host>.

* Edit the SSHD Sever config file   
`sudo vim /etc/ssh/sshd_config`

* Add the following lines and save
```
Match User <username>
   GatewayPorts yes
```

* Restart SSHD service  
`sudo service sshd restart`


#### Setup Remote Port Forward from Local Sytem To Remote Host

`ssh -f -N -R <bind_address>:<remote_port>:localhost:<local_port> <username>@<remote_host>`

Bind address is mandatory and the options can be found [here](https://superuser.com/questions/588591/how-to-make-ssh-tunnel-open-to-public)

#### Example

If you want anyone on the internet to connect to your computer via SSH through a remote host, then you need to do the following on your computer:  
`ssh -f -N -R 0.0.0.0:22022:localhost:22 me@my-remote-server`

Afterwards you can connect to your computer from anywhere on the internet using:  
`ssh me@my-remote-server -p 22022`
