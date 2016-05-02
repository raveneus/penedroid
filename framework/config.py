import ConfigParser
import imp
global cwd

def getTokenColon(line):
    token = ""
    for letter in line:
        if letter != ":":
            token += letter
        else:
            break
    return token

f = open("config/cwd.txt", "r")
cwd = f.read()
f.close()
global y = {}
parser = ConfigParser.ConfigParser()
def getConfig(configFile):
    parser.read(configFile)
    att = eval(parser.get("prf", "att"))
    util = eval(parser.get("prf", "util"))
    conf = [att, util]
    return conf
def load(att, util):
    for module, info in att.items():
        m = imp.load_source(module, cwd + "/modules/" + module + "/" + getTokenColon(info) + ".py")
        if y[getTokenColon(info)[:-3]]:
            print "[-] Two modules with the same name."
        else:
            y[module] = m
    for module in util.keys():
        m = imp.load_source(module, cwd + "/modules/" + module + "/" + module + ".py")
        if y[module]:
            print "[-] Two modules with the same name."
        else:
            y[module] = m

