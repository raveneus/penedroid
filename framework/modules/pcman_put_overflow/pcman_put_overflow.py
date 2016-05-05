import ftplib
import cmd

def getToken(line):
    token = ""
    for letter in line:
        if letter != " ":
            token += letter
        else:
            break
    return token

class pcmanPutOverflowMenu(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.shellType = ["bind"]
    self.user = ["anonymous"]
    self.passwd = ["anonymous@exmaple.com"]
  def help_help(self):
    print "Usage: help [cmd]"
    print "cmd    the command to get help on"
    print "help: show help on a command or list commands"
  def help_set(self):
    print "Usage: set [var] = [val]"
    print "var    variable to set"
    print "val    value to set variable to"
    print "set: set a variable to a value"
    print "Note: you MUST use it exactly as shown: no set [var]=[val]!"
  def do_set(self, args)
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and descriptions"
  def do_show(self, args)
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the pcman_put_overflow context"
  def do_exit(self, args):
    if args:
      return
    return True
  def help_start(self):
    print "Usage: start"
    print "start: start the attack"
  def do_start(self, args)
