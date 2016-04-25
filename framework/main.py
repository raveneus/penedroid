import os
import sys
import ftplib
import cmd
import config
global y
global cwd

cwd = config.cwd
attutil = config.getConfig(cwd + "/config/config.conf")
config.load(attutil[0], attutil[1])
y = config.y

