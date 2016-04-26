import cmd
from socket import *

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
        self.quick = [False]
    def help_help(self):
        print "Usage: help [cmd]"
        print "cmd    command to get help on"
        print "help: show help on a command or list commands"
    def do_set(self, args):
        if !args:
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
        s = socket(AF_INET, SOCK_STREAM)
        if self.quick[0] != False:
            
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
def main():
    scanmenu = scanMenu()
    scanmenu.cmdloop()
if __name__ == __main__:
    main()
