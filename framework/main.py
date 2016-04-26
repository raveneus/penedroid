import os
import ftplib
import cmd
from socket import *
import config
global y
global cwd

cwd = config.cwd
attutil = config.getConfig(cwd + "/config/config.conf")
config.load(attutil[0], attutil[1])
y = config.y

class menu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "pdf% "
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    the command to get help on"
        print "help: show help on a command or list commands"
    def do_util(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        util = utilMenu()
        util.cmdloop(self.prompt[:-1] + ":util% ")
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
        att.cmdloop(self.prompt[:-1] + ":attack% ")
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
    def do_spawn(self, args):
        if args:
            print "*** Argument number: need 0"
            return
        os.system("/system/bin/sh")
    def help_spawn(self):
        print "Usage: spawn"
        print "spawn: spawn a shell"
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
    def 
