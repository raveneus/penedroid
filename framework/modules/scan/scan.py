import cmd
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
import threading
from sys import stdout

class scanThread(threading.Thread):
    def __init__(self, ip, stdout):
        threading.Thread.__init__(self)
        self.ip = ip
        self.stdout = stdout
    def run(self):
        s = socket(AF_INET, SOCK_STREAM )
        for port in range(1, 5000):
            try:
                s.connect((self.ip, port))
                self.stdout.write("[+]Port %d open\n" % port)
            except:
                pass
        s.close()
class quickScanThread(threading.Thread):
    def __init__(self, ip, stdout):
        threading.Thread.__init__(self)
        self.ip = ip
        self.stdout = stdout
    def run(self):
        s = socket(AF_INET, SOCK_STREAM)
        ports = {1:"TCPMUX", 5:"Remote Job Entry", 7:"ECHO", 18:"Message Send Protocol", 20:"FTP Data", 21:"FTP Control", 22:"SSH", 23:"Telnet", 25:"SMTP", 29:"MSG ICP", 37:"Time", 42:"Nameserv", 43:"Whois", 49:"Login", 53:"DNS", 69:"TFTP", 70:"Gopher Services", 79:"Finger", 80:"HTTP", 103:"X.400 Standard", 108:"SNA Gateway Access Server", 109:"POP2", 110:"POP3", 115:"SFTP", 118:"SQL Services", 119:"Newsgroup", 137:"NetBIOS", 138:"NetBIOS", 139:"NetBIOS", 143:"IMAP", 150:"NetBIOS", 156:"SQL Server", 161:"SNMP", 179:"Border Gateway Protocol", 190:"Gateway Access Control Protocol", 194:"IRC", 197:"Directory Location Service", 389:"Lightweight Directory Access Protocol (LDAP)", 443:"HTTPS", 444:"Simple Network Paging Protocol", 445:"SMB", 547:"DHCP Server", 1080:"Socks"}
        for port in ports.keys():
            try:
                s.connect((self.ip, port))
                self.stdout.write("[+]Port %d (%s) open." % (port, ports[port]))
            except:
                pass
        s.close()
def getToken(line):
    token = ""
    for letter in line:
        if letter != " ":
            token += letter
        else:
            break
    return token
class scanMenu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.ip = ["ftp.debian.org"]
        self.quick = [True]
        self.prompt = "pdf-console:util(scan)% "
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    command to get help on"
        print "help: show help on a command or list commands"
    def do_set(self, args):
        if len(args) < 1:
            self.help_set()
            return
        var = getToken(args)
        val = args[len(var):][3:]
        if var == "ip" or var == "IP":
            self.ip[0] = val
        elif var == "quick":
            if eval(val) != True and eval(val) != False:
                print "*** Value not expected type: boolean needed, but found " + type(eval(val))
                return
            self.quick[0] = eval(val)
        else:
            print "*** Variable not found: " + var
        print "[*]" + var + " => " + val
    def help_set(self):
        print "Usage: set [var] = [val]"
        print "var    variable to set"
        print "val    value to set variable to"
        print "set: set a variable to a value"
        print "Note: you MUST use it exactly as shown: no set [var]=[val]!"
    def do_exit(self, args):
        if args:
            print "*** Argument number: needed 0"
            return
        return True
    def help_exit(self):
        print "Usage: exit"
        print "exit: exit the PeneDroid interpreter"
    def do_start(self, args):
        if args:
            print "*** Argument number: needed 0"
            return
        for let in "abcdefghijklmnopqrstuvwxyz":
            if let in self.ip[0]:
                self.ip[0] = gethostbyname(self.ip[0])
        if self.quick[0] != True:
            scanner = scanThread(self.ip[0], stdout)
            scanner.start()
        elif self.quick[0] == True:
            scanner = quickScanThread(self.ip[0], stdout)
            scanner.start()
        else:
            print "*** Unknown error"
            return
    def help_start(self):
        print "Usage: start"
        print "start: start the scan"
    def do_show(self, args):
        if args != "options":
            print "*** Unknown argument: " + args
            return
        print "Options for scan:"
        print "========================"
        print "ip    " + val + "    ip or hostname of the target"
        print "quick    " + val + "    True/False (quick scan)"
    def help_show(self):
        print "Usage: show options"
        print "show options: show the variables, current value, and description"
def main(s):
    scanmenu = scanMenu()
    scanmenu.cmdloop("pdf-console:" + upmenu + "(scan)% ")
if __name__ == '__main__':
    main("")
