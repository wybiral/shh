# shh

ssh is a library for creating Tor [hidden services](https://www.torproject.org/docs/hidden-services.html.en) from within a Python program.

## Download the code

```git clone https://github.com/wybiral/shh.git```

## Install the Python module

```
cd shh
python setup.py install
```

## Serve a directory as a Tor hidden service

In order to start a hidden server you'll need to have [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en#downloads) open.

### Without a key file
The quickest way to serve a directory through a hidden service is to run it ephemerally without a key file. After running the following command the .onion where your directory is accessible address will be returned to the console.
```
cd /Some/Directory/To/Serve
python -m shh
```

### With a key file
If you want to persist an .onion address you'll need to supply a key file. Note that if the key file you supply in the command line doesn't exist it will be created (with a newly generated key).
```
cd /Some/Directory/To/Serve
python -m shh --key=/Path/To/Keyfile
```
**Warning: Don't place your key file within the directory you're serving!**
