import ftblib
import cmd
import token

class ftpanonMenu(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.ip = []
    self.tls = []
  def help_help(self):
    print "Usage: help [cmd]"
    print "cmd    command to get help on"
    print "help: show help on a command or list commands"
  def do_set(self, args):
    var = token.getToken(args);
    val = args[len(var):][3:]
    if var == "ip" or var == "IP":
      self.ip[0] = val
    elif var == "tls" or var == "TLS":
      if eval(val) == True or eval(val) == False:
        print "*** Value not expected type: boolean needed, but found " + type(eval(val))
        return
      self.tls[0] = eval(val)
    else:
      print "*** Variable not found: " + var
      return
  def help_set(self):
    print "Usage: set [var] = [val]"
    print "var    variable to set"
    print "val    value to set variable to"
    print "set: set a variable to a value"
    print "Note: you MUST use it exactly as shown: no set [var]=[val]!"
  def do_exit(self, args):
    if args:
      print "*** Argument number: needed 0"
      return
    return True
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the util context"
  def do_start(self, args):
    if args:
      print "*** Argument number: needed 0"
      return
    if self.tls[0] != True:
      ftp = ftplib.FTP(self.ip[0])
      try:
        ftp.login()
        print "[+]FTP anonymous login (user:anonymous&pass:anonymous@) successful on " + self.ip[0] + "!"
      except:
        print "[-]FTP anonymous login failed on " + self.ip[0] + "! :("
    elif self.tls[0] == True:
      ftps = ftplib.FTP_TLS(self.ip[0])
      try:
        ftps.login()
        print "[+]FTP anonymous login (user:anonymous&pass:anonymous@) successful on " + self.ip[0] + "!"
      except:
        print "[-]FTP anonymous login failed on " + self.ip[0] + "! :("
    else:
      print "*** Unknown error"
  def help_start(self):
    print "Usage: start"
    print "start: start the attempt"
  def do_show(self, args)
  def help_show(self)

    Status API Training Shop Blog About 

