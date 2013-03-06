#include <SPI.h>
#include <Ethernet.h>

int ledYel = 9;

byte mac[] = { 
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = { 
  192,168,1, 177 };

Server server(5000);

void setup()
{
  pinMode(ledYel, OUTPUT);
 Serial.begin(9600);
  Ethernet.begin(mac, ip);
  server.begin();
}

void loop()
{
  // listen for incoming clients
  Client client = server.available();
  if (client) {
    String msg = "";
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        msg += c;
        if (c == '\n') {
          Serial.println("Message from Client:"+msg);//print it to the serial
          client.println("You said:"+msg);//modify the string and send it back
          if(msg.length() == 9) {
            char* cmd = (char*)malloc(5);
            char* param = (char*)malloc(5);
            (msg.substring(0,4)).toCharArray(cmd, 5);
            (msg.substring(4)).toCharArray(param, 5);
            Serial.println("Command is:"+msg.substring(0,4));
            Serial.println("Param is:"+msg.substring(4));
            controlCloud(atoi(cmd), atoi(param));
            Serial.println(atoi(cmd));
            Serial.println(atoi(param));
          }
          msg="";
        }
      }
    }
    delay(1);
    // close the connection:
    client.stop();
  }
}

void controlCloud(int cmd, int params) {
  switch(cmd) {
    //RED_PWM
  case 1: 
    break;

    //YELLOW_PWM
  case 2:
    break;

    //GREEN_PWM
  case 3:
    break;

    //BLUE_PWM
  case 4:
    break;

    //RED
  case 5:
    break;

    //WHITE
  case 6:
    break;

    //YELLOW
  case 7:
    break;

    //RGB
  case 8:
    break;

    //SUNSHINE
  case 11:
    for(int i=0; i<=155; i++) {
      analogWrite(ledYel, i);
      delay(i+50);
    }
    
    break;

    //RAIN
  case 12:
    break;

    //LIGHTNING
  case 13:
    break;

    //RANDOM
  case 14:
    break;

    //SHUTDOWN
  case 21:
    digitalWrite(ledYel, LOW);
    break;
  }
}







