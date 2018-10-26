# SublimeCloogle
A small Sublime Text 3 plugin which allows to search for [Clean](http://clean.cs.ru.nl/) definitions. It is based on a modified [cloogle.py](https://gitlab.science.ru.nl/cloogle/cloogle-py) module, originally created by Camil Staps.

### Usage
Bind a key to execute the command "cloogle_search":
```
{ "keys": ["ctrl+shift+c"], "command": "cloogle_search"}
```

The command searches for the currently selected text using the [Cloogle](https://gitlab.science.ru.nl/cloogle/cloogle-org) search engine.

### TODO
* Better formatting of the result
* Only show exact matches
* Support some Cloogle options
