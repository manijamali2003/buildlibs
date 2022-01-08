from pyabr.core import *
import os,subprocess

su = files.readall ('/proc/info/su')

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

os.environ['HOME'] = user

subprocess.call('cd /stor/usr/app/ && ./example',shell=True)