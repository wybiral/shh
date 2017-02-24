# shh

ssh is a library built around [Stem](https://stem.torproject.org/) for creating Tor [hidden services](https://www.torproject.org/docs/hidden-services.html.en) from within a Python program. It also includes a small command line tool for serving local ports or creating simple file servers as hidden services.

In order to start a hidden server you'll need to have [Tor Browser](https://www.torproject.org/projects/torbrowser.html.en#downloads) open or the Tor daemon running with a [control port] (http://www.thesprawl.org/research/tor-control-protocol/) (shh defaults to port 9151 but this can be changed in your code).

- [How to install](https://github.com/wybiral/shh/wiki/Installation)
- [Command line usage](https://github.com/wybiral/shh/wiki/Command-Line-Tool)
