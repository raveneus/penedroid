import os
import sys
import ftplib
import cmd
import config
global y
global cwd

cwd = config.cwd
config.load(config.getConfig(cwd + "/config/config.conf"))
y = config.y

