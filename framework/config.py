import ConfigParser
import imp
global cwd
import token.py
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
    for module in att:
        m = imp.load_source(module, cwd + "/modules/" + module + "/" + module + ".py")
        if y[module]:
            print "[-] Two modules with the same name."
        else:
            y[module] = m
    for module in util:
        m = imp.load_source(module, cwd + "/modules/" + module)
        if y[module]:
            print "[-] Two modules with the same name."
        else:
            y[module] = m

