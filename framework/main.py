#import statements
import os
import ftplib
import cmd
from socket import *
import config
#global variables
global y
global cwd
global attutilL
global menus
global util_help_str
global nix_help_str
global win_help_str
global pc
#version number
version = "0.2"
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
#set pc
pc = config.pc
#load/import modules
config.load(attutilL[0], attutilL[1])
#set y (global array with module objects)
y = config.y

#define menus
class attMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "pdf-console:attack% "
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    the command to get help on"
        print "help: show help on a command or list commands"
    def do_os(self, args):
        if args == "linux":
            menus[0].cmdloop()
        elif args == "windows":
            menus[1].cmdloop()
        else:
            print "*** Unknown argument: %s" % args
            return
    def help_os(self):
        print "Usage: os [os]"
        print "os    os to set (linux/windows) (sorry... no macs :) )"
        print "os: set the os of the target"
    def do_exit(self, args):
        if args:
            print "*** Argument number: needed 0"
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
        util = menus[2]
        util.cmdloop()
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
        att.cmdloop()
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
        self.prompt = "pdf-console:util% "
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
            print "*** Argument number: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the utility context"
class linuxMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "pdf-console:attack(linux)% "
    def do_exit(self, args):
        if args:
            print "*** Argument number: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the linux context"
class windowsMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "pdf-console:attack(windows)% "
    def do_exit(self, args):
        if args:
            print "*** Argument number: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the windows context"

#define a function to load functions into menus
def loadFunc(attutil):
    util_help_str = "\nDocumented commands (type help [topic]): \n========================================\nexit  help  spawn\n\nCommands from modules (type help[topic]): \n========================================\n"
    utilmenu = utilMenu()
    for util in attutil[1].keys():
        util_help_str += util + "  "
        setattr(utilmenu, "do_" + util, y[util].main)
        def tmp(self):
            print "Usage: " + util
            print "%s: %s" % (util, attutil[1][util])
        setattr(utilmenu, "help_" + util, tmp)
    util_help_str += "\n"
    def tmp(self):
        print util_help_str
    setattr(utilmenu, "do_help", tmp)
    nixmenu = linuxMenu()
    winmenu = windowsMenu()
    nix_help_str = "\nDocumented commands (type help [topic])\n========================================\nexit  help\n\nCommands from modules (type help [topic]): \n========================================\n"
    win_help_str = "\nDocumented commands (type help [topic])\n========================================\nexit  help\n\nCommands from modules (type help [topic]): \n========================================\n"
    for module, info in attutil[0].items():
        name = getTokenColon(info)
        #tests to see what os is it and load into appropriate menu
        if getTokenColon(info[len(getTokenColon(info)) + 1:]) == "linux":
            nix_help_str += name + "  "
            setattr(nixmenu, "do_" + name, y[name].main)
            def temp(self):
                print "Usage: %s" % name
                #the next line takes the third thing in info (description) : "name:os:desc" for attack modules
                print "%s: %s" % (name, info[len(getTokenColon(info[len(getTokenColon(info)) + 1:])) + 1:])
            setattr(nixmenu, "help_" + name, temp)
        if getTokenColon(info[len(getTokenColon(info)) + 1:]) == "windows":
            win_help_str += name + "  "
            setattr(winmenu, "do_" + name, y[name].main)
            def temp(self):
                print "Usage: %s" % name
                #the next line takes the third thing in info (description) : "name:os:desc" for attack modules
                print "%s: %s" % (name, info[len(getTokenColon(info[len(getTokenColon(info)) + 1:])) + 1:])
            setattr(winmenu, "help_" + name, temp)
    nix_help_str += "\n"
    win_help_str += "\n"
    def tmp(self):
        print nix_help_str
    setattr(nixmenu, "do_help", tmp)
    def tmp(self):
        print win_help_str
    setattr(winmenu, "do_help", tmp)
    return [nixmenu, winmenu, utilmenu]
#load the functions
menus = loadFunc(attutilL)

#display awesome banner
pc_banner = """
..............-.:/-...-......................................-::-...............
................+ys-........................................-oyo-...............
................./yy:......................................-syo-................
................../yy/....................................:sy+-.................
...................:yy/.........-:///+++++++//::--.......:sy+...................
....................:sy/.-/+os+-.:oyyyyyyyyyyyyyyyso+/:-:yy/....................
....................-/yyyyyyyyyy+-.:+syyyyyyyyyyyyyyyyyyyy+-....................
................../oyyyyyyyyyyyyyyo:..:+syyyyyyyyyyyyyyyyyyyo/-.................
...............:oyyyyyyyyyyyyyyyyyyys+:..-/+syyyyyyyyyyyyyyyyyyo/...............
............./syyyyyyyyyyyyyyyyyyyyyyyyso/-..-:/+syyyyyyyyyyyyyyys/.............
...........:syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyso/:-...-:/+oossyyyyyyyyy/...........
.........-oyyyyyyyyys+:::+yyyyyyyyyyyyyyyyyyyyyyso..........---:::///:..........
......../yyyyyyyyyys-.....-yyyyyyyyyyyyyyyyyyyyyyy:.............-:::::::........
.......+yyyyyyyyyyys......-yyyyyyyyyyyyyyyyyyyyyyys-...........-yyyyyyyyo.......
......+yyyyyyyyyyyyys/---/syyyyyyyyyyyyyyyyyyyyyyyys:........./yyyyyyyyyyo......
....`/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo/-.`.-/syyyyyyyyyyyyo.....
.```:yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/`...
````syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.```
```-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy/```
```/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyo```
```+yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys```
```.---::::------------------------------------------------------------------```
````-oyyyyyyo:.```````````````````````````````````````````````````./oyyyyyo/.```
```+yyyyyyyyyys/-.``````````````````````````````````````````````-/syyyyyyyyys-``
``:yyyyyyyyyyyyyyyyo/:-```````````````````````````````````.-/osyyyyyyyyyyyyyys.`
``:yyyyyyyyyyyyyyyyyyyyys+:-.````````````````````````-:+osyyyyyyyyyyyyyyyyyyyy.`
```+yyyyyyyyyyyyyyyyyyyyyyyyyso/:.`````````````.:/osyyyyyyyyyyyyyyyyyyyyyyyyy/``
````:oyyyyyyyyyyyyyyyyyyyyyyyyyyyys+-````.-/+oyyyyyyyyyyyyyyyyyyyyyyyyyyyyys:```
```````-::--:+oyyyyyyyyyyyyyyso/:.``.:/oyyyyyyyyyyyyyyyyyyyyyyyyyyso/::::-``````
````````````````.:/osyyyo+:.``.-/+syyyyyyyyyyyyyyyyyyyyyyyyyyo+:-`` ````````````
        ``           ````-:+oyyyyyyyyyyyyyyyyyyyyyyyyyys+/-.  ``````         `  
                   .:/osyyyyyyyyyyyyyyyyyyyyyyyyyso/:.``.-/:.`                  
            ``-:+syyyyyyyyyyyyyyyyyyyyyyyyyyo+:-```-:+syyyyyyys+:-``            
    `:+osssosyyyyyyyyyyyyyyyyyyyyyyyyys+/-.``.:/osyyyyyyyyyyyyyyyyysoooso+/.    
   :yyyyyyyyyyyyyyyyyyyyyyyyyyyyso/:.`     `-/osyyyyyyyyyyyyyyyyyyyyyyyyyyyy+`  
  -yyyyyyyyyyyyyyyyyyyyyyyys+/-``               `.:+oyyyyyyyyyyyyyyyyyyyyyyyy+` 
  /yyyyyyyyyyyyyyyyyyso/:.                            .-/osyyyyyyyyyyyyyyyyyys. 
  .syyyyyyyyyyyyo+:-`                                      `-:+syyyyyyyyyyyyy+` 
   .osyyyyyyyo-                                                  .+syyyyyyys/`  
     `-////:.                                                      `:/+o+/-` 
"""

android_banner = """

&&&&&&&&&%#&&&&&&&&&&&&&&&&&&&&&&&&&%#&&&&&&&&&
&&&&&&&&&&*(&&&&&&&&&&&&&&&&&&&&&&*&&&&&&&&&&
&&&&&&&&&&&//&&&&&&&&&%%%&&&&&&&&&(*&&&&&&&&&&&
&&&&&&&&&&&&//#/**%&(***********(//&&&&&&&&&&&&
&&&&&&&&&&%*********(&&(************#&&&&&&&&&&
&&&&&&&&/**************%&***********/&&&&&&&&
&&&&&&/*******************/#%&&&%(/*****/&&&&&&
&&&&%******(&&*************/&&&&&&&&&&&&&&&&&
&&*******/&&&/**************(&&&&&&/*****(&&&
&&%*****************************/%%/********#&&
@@/******************************************@@
@&*******************************************%@
@%*******************************************#@
@@%****%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(***#@@
@(*******/%@@@@@@@@@@@@@@@@@@@@@@@@@@%(*******@
@/************/#@@@@@@@@@@@@@@@&(*************&
@@/*****************/%@@@&(******************%@
@@@@@@@@%/******#&@@%/****************/%@@@@@@@
@@@@@@@@@@@@@@%/****************/%@@@@@@@@@@@@@
@@@@@@@@@&(****************/#@@***(&@@@@@@@@@
@@#*******************#&@@#/****************(@@
@/**************(&@@@@@@@@@@@@#***************@
@/********/%@@@@@@@@@@@@@@@@@@@@@@@%/*********@

"""

if pc == "yes":
    print pc_banner
else:
    print android_banner

print "PeneDroid Console v" + version + " -- an FTP exploitation framework"
print "(c) Raveneus 2016\n"

#now, run the main menu
menuMain = menu()
menuMain.cmdloop()
