import socket

# protocol is: HEADER(4 byte, command code) BODY(4 byte, value for single led control) 
class ArduinoSocket:
    RED_PWM = 1
    YELLOW_PWM = 2
    GREEN_PWM = 3
    BLUE_PWM = 4
    RED = 5
    WHITE = 6
    YELLOW = 7
    RGB = 8

    SUNSHINE = 11
    RAIN = 12
    LIGHTNING = 13
    RANDOM = 14
    
    SHUTDOWN = 21

    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        except Exception, e:
            print e

    def close(self):
        self.socket.close()

    def sendPackage(self, header, body):
        data = str(int(header)).zfill(4) + str(int(body)).zfill(4) + "\n"
        print data
        try:
            self.socket.send(data)
        except Exception, e:
            print e

