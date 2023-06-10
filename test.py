import PyV8
import time
import _winreg
s = open('details_8f3759.js', 'rb').read()

class K2WScript(PyV8.JSClass) :
    def Sleep(self, x) :
        time.sleep(x/1000.)
        
    def CreateObject(self, progid) :
        print '[*] CreateObject :', progid
        if progid.lower() == 'wscript.shell' :
            return K2WshShell()
        elif progid.lower() == 'msxml2.xmlhttp' :
            return K2XMLHTTP()
        elif progid.lower() == 'adodb.stream' :
            return K2Stream()
            
class K2WshShell(PyV8.JSClass) : 
    def ExpandEnvironmentStrings(self, x) :
        s = _winreg.ExpandEnvironmentStrings(unicode(x))
        print '[*] ExpandEnvironmentStrings :', x
        print '    [-] :', s
        return s
    def Run(self, x, y, z) :
        print '[*] WshShell.Run :'
        print '    [-] :', x  
        
class K2XMLHTTP(PyV8.JSClass) : 
    def open(self, x, y, z) :
        print '[*] XMLHTTP.open :'
        print '    [-] :', x  
        print '    [-] :', y  
        print '    [-] :', z
    def send(self) :
        pass
        
class K2Stream(PyV8.JSClass) :
    def open(self) :
        pass
    def write(self, x) :
        pass
    def SaveToFile(self, x, y) :
        print '[*] SaveToFile :', x
    def close(self) :
        pass
        
class Global(PyV8.JSClass):
    WScript = K2WScript()


ctx = PyV8.JSContext(Global())
ctx.enter()
ctx.eval(s)

