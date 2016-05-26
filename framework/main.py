#import statements
import os
import ftplib
import cmd
from socket import *
import config
global y
global cwd
global attutilL
global menus
#define a token separator with colon: getTokenColon("foo:bar") => "foo"
def getTokenColon(line):
    token = ""
    for letter in line:
        if letter != ":":
            token += letter
        else:
            break
    return token
#get current working directory
cwd = config.cwd
#get the array
attutilL = config.getConfig(cwd + "/config/config.conf")
#load/import modules
config.load(attutilL[0], attutilL[1])
#set y (global array with module objects)
y = config.y

#define menus
class attMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    the command to get help on"
        print "help: show help on a command or list commands"
    def do_os(self, args):
        if args == "linux":
            menus[0].cmdloop("pdf-console:attack(linux)% ")
        elif args == "windows":
            menus[1].cmdloop("pdf-console:attack(windows)% ")
        else:
            print "*** Unknown argument: %s" % args
            return
    def help_os(self):
        print "Usage: os [os]"
        print "os    os to set (linux/windows) (sorry... no macs :) )"
        print "os: set the os of the target"
    def do_exit(self, args):
        if args:
            print "*** Number of arguments: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the attack context"
class menu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "pdf-console% "
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    the command to get help on"
        print "help: show help on a command or list commands"
    def do_util(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        util = self.menus[2]
        util.cmdloop("pdf-console:util% ")
    def help_util(self):
        print "Usage: util"
        print "util: change into the utility context"
    def do_exit(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exits the PeneDroid Framework interpreter"
    def do_attack(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        att = attMenu()
        att.cmdloop("pdf-console:attack% ")
    def help_attack(self):
        print "Usage: attack"
        print "attack: switch into the attack context"
    def do_shell(self, args):
        os.system(args)
    def help_shell(self):
        print "Usage: shell [cmd]"
        print "cmd    command to execute"
        print "shell: execute a command in a shell"
        print "Note: it is acceptable to replace \"shell\" with \"!\"."
    def do_port(self, args):
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect((args, 21))
            s.close()
            print "[+]" + args + " port 21: [open]"
        except:
            s.close()
            print "[-]" + args + " port 21: [closed/filtered]"
    def help_port(self):
        print "Usage: port [host]"
        print "host    the IP or hostname of the target"
        print "port: check to see if port 21 (FTP) is open"
class utilMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    the command to get help on"
        print "help: show help on a command or list commands"
    def do_spawn(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        os.system("/system/bin/sh")
    def help_spawn(self):
        print "Usage: spawn"
        print "spawn: spawn a shell"
    def do_exit(self, args):
        if args:
            print "*** Number of arguments: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the utility context"
class linuxMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
    def do_exit(self, args):
        if args:
            print "*** Number of arguments: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the linux context"
class windowsMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
    def do_exit(self, args):
        if args:
            print "*** Number of arguments: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the windows context"

#define a function to load functions into menus
def loadFunc(attutil):
    utilmenu = utilMenu()
    for util in attutil[1].keys():
        setattr(utilmenu, "do_" + util, y[util].main)
        def tmp(self):
            print "Usage: " + util
            print "%s: %s" % (util, attutil[1][util])
        setattr(utilmenu, "help_" + util, tmp)
        nixmenu = linuxMenu()
        winmenu = windowsMenu()
    for module, info in attutil[0].items():
        name = getTokenColon(info)
        #tests to see what os is it and load into appropriate menu
        if getTokenColon(info[len(getTokenColon(info)) + 1:]) == "linux":
            setattr(nixmenu, "do_" + name, y[att].main)
            def temp(self):
                print "Usage: %s" % name
                #the next line takes the third thing in info (description) : "name:os:desc" for attack modules
                print "%s: %s" % (name, info[len(getTokenColon(info[len(getTokenColon(info)) + 1:])) + 1:])
            setattr(nixmenu, "help_" + name, temp)
        if getTokenColon(info[len(getTokenColon(info)) + 1:]) == "windows":
            setattr(winmenu, "do_" + name, y[att].main)
            def temp(self):
                print "Usage: %s" % name
                #the next line takes the third thing in info (description) : "name:os:desc" for attack modules
                print "%s: %s" % (name, info[len(getTokenColon(info[len(getTokenColon(info)) + 1:])) + 1:])
            setattr(winmenu, "help_" + name, temp)
    return [nixmenu, winmenu, utilmenu]
#load the functions
menus = loadFunc(attutilL)

#now, run the main menu
menu().cmdloop()
