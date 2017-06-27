# About
How to setup a private or custom PyPi Server. Currently the documentation only shows how to create an HTTP based PyPi server.

# How to setup custom PyPi server [HTTP Only]
In order to setup pypiserver on your local system, the following things need be to configured:

### Install Pypiserver
* `pip install pypiserver`

### Create pypiserver directory
This is to store the packages directory as well the authentication htpasswd.txt file.
* `mkdir ~/pypiserver`

### Create packages directory
This is the directory that will contains the private python packages or modules. The name and location of the this directory can be anything.
* `mkdir -p ~/pypiserver/packages`

### Creating Apache-line authentication (htpasswd)
The original directions can be found [here](https://github.com/pypiserver/pypiserver#apache-like-authentication-htpasswd).
* `pip install passlib`
* `apt-get install apache-utils # for htpasswd`

### Create users and passwords for uploading onto pypiserver
Using htpasswd the default encryption is MD5. We will use a file called htpasswd.txt which contains the users and encryted passwords.
* `cd ~/pypiserver`
* `touch htpasswd.txt`
* `htpasswd htpasswd.txt <some-username> # It will prompt for password`

### Run the server
If we would like to tun the pypiserver on port <server-port> using htpasswd.txt for authentication and ~/pypiserver/pakages for the packages to serve.
* `cd ~/pypiserver`
* `pypi-server -p <server-port> -P htpasswd.txt ~/pypiserver/packages &`

# How to upload packages to custom PyPi server [HTTP Only]
The following things need to be configure in order to upload packages onto the custom pypiserver:

### Create & configure ~/.pypirc file
The `~/.pypirc` contains the configuration the offical pypi and the custom pypi servers. Create the ~/.pypirc file and add the follwing configurations to it. Don't enter your password, you will be prompted for it when required. NOTE : Make sure that the custom PyPi server has your username and password stored in its `~/pypiserver/htpasswd.txt` file.
```
[distutils]
index-servers =
  pypi
  local

[pypi]
username:<your-username>

[local]
repository: http://<server-ip>:<server-port>
username:<your-username>
```

### Upload python package to custom PyPi server.
Assuming you have a ready-to-upload python package directory named foobar which contains the setup.py file and we would like to upload it to our custom PyPi server named local in our  ~/.pypirc.
* `cd ~/pypackages/foobar`
* `python setup.py sdist upload -r local`

# How to download packages from custom PyPi server [HTTP Only]

### Add extra-index-url parameter to ~/.pip/pip.conf
This is the an optional step to avoid having to use extra-index-url parameter everytime you have to install a package using pip. Create a file called ~/.pip/pip.conf and add the following to it:
```
[global]
extra-index-url = http://<server-ip>:<server-port>/simple/
```

### Install package from custom PyPi server
Use the following command in case the custom PyPi server does not have https support.
* `pip install foobar --trusted-host <server-ip>`

# Adding HTTPS Support
TODO
