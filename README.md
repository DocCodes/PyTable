# PyTable

[![Build Status](https://img.shields.io/travis/DocCodes/PyTable.svg)](https://travis-ci.org/DocCodes/PyTable)
[![Release](https://img.shields.io/github/release/doccodes/pytable.svg?)](https://github.com/doccodes/pytable/releases)
[![Beta](https://img.shields.io/github/release/doccodes/pytable/all.svg?label=nightly)](https://github.com/doccodes/pytable/releases)

## Installation
1. First download this git
2. Change to the pytable directory
3. Then use pip3 to install it

### Windows
*See above to obtain code*
```
cd pytable
pip3 install .
```
### Linux / macOS
```
cd ~/Downloads
git clone https://github.com/DocCodes/pytable
cd pytable
sudo -H pip3 install .
```

## How-To Use
```
import table

r = [
   ["Game", "Developer", "Year"],
   ["Terraria", "Re-Logic", 2011],
   ["Minecraft", "Mojang", 2011],
   ["Skyrim", "Bethesda", 2011],
   ["Fallout 4", "Bethesda", 2015]
]
t = table.table(r)
```
output
```
-----------------------------
|   Game   |Developer |Year |
-----------------------------
|Terraria  |Re-Logic  |2011 |
-----------------------------
|Minecraft |Mojang    |2011 |
-----------------------------
|Skyrim    |Bethesda  |2011 |
-----------------------------
|Fallout 4 |Bethesda  |2015 |
-----------------------------
```


## Requirements
To install any modules use `pip3 install (module)`
* pytest
