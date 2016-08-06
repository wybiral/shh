# shh

ssh is a library built around [Stem](https://stem.torproject.org/) for creating Tor [hidden services](https://www.torproject.org/docs/hidden-services.html.en) from within a Python program. It also includes a small command line tool for serving any directory as a hidden service and providing you with the .onion link to access it.

In order to start a hidden server you'll need to have [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en#downloads) open.

## Download the code

```git clone https://github.com/wybiral/shh.git```

## Install the Python module

```
cd shh
python setup.py install
```

## Serve a directory as a Tor hidden service

#### Without a key file
The quickest way to serve a directory through a hidden service is to run it ephemerally without a key file. After running the following command the .onion where your directory is accessible address will be returned to the console.
```
cd /Some/Directory/To/Serve
python -m shh -s
```

#### With a key file

*Warning: Don't place your key file within the directory you're serving!*

If you want to persist an .onion address you'll need to supply a key file. Note that if the key file you supply in the command line doesn't exist it will be created (with a newly generated key).
```
cd /Some/Directory/To/Serve
python -m shh -s --key=/Path/To/Keyfile
```

## Serve any local port (don't create a server)
If you already have a server running on a port and want to turn it into a temporary hidden service, run this command:
```
python -m shh -p YOUR_PORT
```
