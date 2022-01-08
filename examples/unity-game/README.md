# Unity Game Project

- Copy example to `packs/`
- Set `compile: Yes` in `manifest`
- Build your **Unity game** with **Linux x86_64 binary files**
- Copy your compiled game (with data folder) in `data/usr/app`
- Write Python Script for running **Unity game file** in `/usr/app/` in `code` directory:
```python 
from pyabr.core import *
import os,subprocess

su = files.readall ('/proc/info/su')

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

os.environ['HOME'] = user

subprocess.call('cd /stor/usr/app/ && ./example',shell=True)
```
- Write Desktop entry file in `data/usr/share/applications` with `example.desk` name:
```
name[en]: Example
name[fa]: مثال
logo: @icon/app
exec: example
application: Yes
game: Yes
category: games
pin: No
```
- Copy your Icon game ( should be svg, png, gif or tiff format ) in `data/usr/share/icons`
- For example your icon name is `example.svg` in `data/usr/share/icons` small path name is `@icon/example`
- Set your small path icon name in Desktop entry
```
logo: @icon/app
```