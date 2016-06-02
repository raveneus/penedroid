import ConfigParser
import imp
global cwd
global pc

def getTokenColon(line):
    token = ""
    for letter in line:
        if letter != ":":
            token += letter
        else:
            break
    return token

f = open("config/cwd.txt", "r")
cwd = f.read().rstrip()
f.close()
global y
y = {}
parser = ConfigParser.ConfigParser()
def getConfig(configFile):
    parser.read(configFile)
    att = eval(parser.get("prf", "att"))
    util = eval(parser.get("prf", "util"))
    try:
        pc = parser.get("prf", "pc")
        if pc != "yes":
            print "If you're going to set pc, it must be \"yes\""
    except:
        pc = "no"
    conf = [att, util]
    return conf
def load(att, util):
    for module, info in att.items():
        m = imp.load_source(module, cwd + "/modules/" + module + "/" + getTokenColon(info) + ".py")
        if getTokenColon(info) in y.keys():
            print "[-] Two modules with the same name."
        else:
            y[getTokenColon(info)] = m
    for module in util.keys():
        m = imp.load_source(module, cwd + "/modules/" + module + "/" + module + ".py")
        if module in y.keys():
            print "[-] Two modules with the same name."
        else:
            y[module] = m

