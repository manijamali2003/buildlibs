# Build libs Script
 You can use build libs script for building your Standard Package for Pyabr distro
 
## packs/
Your project should be stored in `packs/` directory.

## buildlibs/
The core of build-libs script stored here.

## How can I create a project?

### Create directories of package
- Create a directory in packs with your package name for example `com.example.example`
- Create three directories in your package folder ( code , control , data )
- Your C/C++/Python code should save in `code` directory

### Writing Manifest
- Write `manifest` file in control directory of your package
```
name: com.example.example
name[en]: Example
name[fa]: مثال
unpack: /
entry: example
license: Free Software
copyright: (c) 2021 Mani Jamali
description: Example build-libs application for Pyabr
version: 1.0.0
build: 1400-10-18
```
- `name` field used for package name; package name should be same as your project name
- Showing name such as `name[en], name[fa], name[tr], name[ch], ...` describe your project name
- `name[en]` is required
- `unpack` field is your unpacking path of your project for example `echo` command stored in `/usr/bin` that you can set unpack in `/usr/bin`
- `entry` is not required but you can run your project with this field directly
- You can put your license name in `license` field
- You can put your copyright in `copyright` field
- You can descript your project in `description` field, don't create a new line at all
- Set your version package in `version` field
- Set your package build date in `build` field, latest build date not inital build date

Save `manifest` in `control/`
### Writing list
In older versions of Pyabr you should write all files stored in `data/` in `list` file in `control/`
But in newer versions you can only create `list` file in `control/` without writing files

### Write compile list
If your project is open-source you can put your C/C++/Python codes in `code` directory, and compile them with compile list

For example:
- Write `example.py` in `code/` directory
```python
print("Hello World")
```
- Save it
- Write compile list
```
example.py:usr/app/example.pyc
```
- Save it
- Open `manifest` file in `controls/`
- Add this field at the end of this file:
```
compile: Yes
```

### Creating Data files

- ***/packs/.../data/usr/app:*** used for executable files
- ***/packs/.../data/usr/share/applications:*** used for desktop application entry files
- ***/packs/.../data/usr/share/icons:*** used for icons
- ***/packs/.../data/usr/share/themes:*** used for themes

### Build project

- Run `build-packs.py` and copy all `.pa` files in `build-packs` folder
- Run `clean.py` for cleaning project
- Run `debug.py` for creating your project in `stor/`

## Examples folder

You can use example projects in this folder

## Publish project in Main repo of Pyabr

After building project you should send your packages `*.pa` in `build-packs` to `manijamali2003@gmail.com` email

- Your subject: 
```text
Pushing an application in Pyabr Operating System
```

- Your text:
```text
package name: [your package name]
package version: [your package version]
developers: [creators and developers]
company: [your company]
source: [Open source or Close source]
all licenses: [please upload or write your license name or license code; if the contents in your project is nonfree you should upload your license]
price: [Price of your project]
```