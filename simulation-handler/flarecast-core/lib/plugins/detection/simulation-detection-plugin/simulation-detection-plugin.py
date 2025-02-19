import threading
import socket
from detector import *
from event import *
import os
import struct

class SimulationDetector(Detector):

    @on_event
    def interpret(self, lifetime):
        return Event(1,1,"simulation", False, time.time(), lifetime, None)

    def run(self):
        s = socket.socket()
        port = int(os.environ.get('FLARECAST_PORT')) #get port from env
        host = '127.0.0.1'
        s.connect((host, port))

        while True:
            #lifetime = pickle.loads(unity_socket.recv(1024))
            lifetime = struct.unpack('f', s.recv(4))[0]
            print("LIFETIME: ", lifetime)
            self.interpret(lifetime)
