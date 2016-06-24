import SocketServer
import sys
from emuBot import *

wheelMode(1)
wheelMode(2)
wheelMode(3)
wheelMode(4)
jointMode(5)
jointMode(6)
jointMode(7)

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while 1:
            self.data = self.request.recv(1024).strip()
            new = self.data.split('\n')
            for i in new:
                if i != "":
                    ID = int(i[0])
                    if ID < 5:
                        moveWheel(ID, int(i[1:]))
                    else:
                        moveJoint(ID, int(i[1:-4]), i[-4:])
               # else:
                #    print(i)
                
if __name__ == "__main__":
    HOST, PORT = "", 9999
    
SocketServer.TCPServer.allow_reuse_address = True
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()



