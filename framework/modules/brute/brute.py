import cmd
import ftplib

def getToken(line):
    token = ""
    for letter in line:
        if letter != " ":
            token += letter
        else:
            break
    return token

upmenu = "util"

class bruteMenu(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.passwdfile = ["rockyou.txt"]
    self.singleUsername = [True]
    self.user = ["admin"]
    self.userfile = ["users.txt"]
  def help_help(self):
    print "Usage: help [cmd]"
    print "cmd    the command to get help on"
    print "help: show help on a command or list commands"
  def do_start(self, args)
  def help_start(self):
    print "Usage: start"
    print "start: start the attempt"
  def do_exit(self, args):
    if args:
      print "*** Argument number: needed 0"
      return
    return True
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the brute-forcer context"
  def do_show(self, args):
    if args != "options":
      print "*** Unknown argument: " + args
      return
    print "Options for brute:"
    print "========================"
    print "pwdfile    " + self.pwdfile[0] + "    password file to try passwords from"
    print "single-username    " + self.singleUsername[0] + "    True/False (use one username)"
    print "user    " + self.user[0] + "    username to crack passwords for"
    print "userfile    " + self.userfile[0] + "    file with usernames in them"
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and description"
  def do_set(self, args)
  def help_set(self):
    print "Usage: set [var] = [val]"
    print "var    variable to set"
    print "val    value to set variable to"
    print "set: set a variable to a value"
    print "Note: you MUST use it exactly as shown: no set [var]=[val]!"
