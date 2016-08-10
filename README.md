# shh

ssh is a library built around [Stem](https://stem.torproject.org/) for creating Tor [hidden services](https://www.torproject.org/docs/hidden-services.html.en) from within a Python program. It also includes a small command line tool for serving local ports or creating simple file servers as hidden services.

In order to start a hidden server you'll need to have [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en#downloads) open.

## Installation

#### Install with pip
```
pip install shh
```
... or ...

#### Install from Github:
```
git clone https://github.com/wybiral/shh.git
cd shh
python setup.py install
```

## Serve local port as hidden service
If you already have a server running on a port and want to turn it into a temporary hidden service, run this command:
```
python -m shh -p YOUR_PORT
```
The console will give you your .onion link once the service is up.

## Serve a directory as a Tor hidden service

#### Without a key file
The quickest way to serve a directory through a hidden service is to run it ephemerally without a key file:
```
cd /Some/Directory/To/Serve
python -m shh -s
```
An .onion link will be provided in the console.
#### With a key file

*Warning: Don't place your key file within the directory you're serving!*

If you want to persist an .onion address you'll need to supply a key file. Note that if the key file you supply in the command line doesn't exist it will be created (with a newly generated key).
```
cd /Some/Directory/To/Serve
python -m shh -s --key=/Path/To/Keyfile
```
