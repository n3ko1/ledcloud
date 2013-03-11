#include <SPI.h>
#include <Ethernet.h>

int ledWhi = 4;
int ledRed = 2;
int ledRedPWM = 3;
int ledYelPWM = 5;
int ledGrePWM = 6;
int ledYel = 7;
int ledRGB = 8;
int ledBluPWM = 9;

int currentMode = 0;
int rainFadeIn = 0;

int musicFast = 0;
int beatCount = 0;

int currMil = 0;
float updateInterval = 3000;

byte mac[] = { 
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = { 
  192,168,1, 177 };

Server server(5000);

void setup()
{
  pinMode(ledWhi, OUTPUT);
  pinMode(ledRed, OUTPUT);
  pinMode(ledRedPWM, OUTPUT);
  pinMode(ledYelPWM, OUTPUT);
  pinMode(ledGrePWM, OUTPUT);
  pinMode(ledYel, OUTPUT);
  pinMode(ledRGB, OUTPUT);
  pinMode(ledBluPWM, OUTPUT);
  currMil = millis();
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
            currentMode = atoi(cmd);
            if(currentMode != 15) {
              updateInterval = 3000;
            }
            controlCloud(atoi(cmd), atoi(param));
            Serial.println(atoi(cmd));
            Serial.println(atoi(param));
          }
          msg="";
        }
      }
      int now = millis();
      if(currentMode != 0 && now - currMil >= updateInterval) {
        updateAnimatedLight(currentMode);
        currMil = millis();
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
    if(params <= 100 && params >= 0) {
      analogWrite(ledRedPWM, params*2.55);
    }
    break;

    //YELLOW_PWM
  case 2:
    if(params <= 100 && params >= 0) {
      analogWrite(ledYelPWM, params*2.55);
    }
    break;

    //GREEN_PWM
  case 3:
    if(params <= 100 && params >= 0) {
      analogWrite(ledGrePWM, params*2.55);
    }
    break;

    //BLUE_PWM
  case 4:
    if(params <= 100 && params >= 0) {
      analogWrite(ledBluPWM, params*2.55);
    }
    break;

    //RED
  case 5:
    if(params == 100) {
      digitalWrite(ledRed, HIGH);
    } 
    else {
      digitalWrite(ledRed, LOW);
    }
    break;

    //WHITE
  case 6:
    if(params == 100) {
      digitalWrite(ledWhi, HIGH);
    } 
    else {
      digitalWrite(ledWhi, LOW);
    }
    break;

    //YELLOW
  case 7:
    if(params == 100) {
      digitalWrite(ledYel, HIGH);
    } 
    else {
      digitalWrite(ledYel, LOW);
    }
    break;

    //RGB
  case 8:
    if(params == 100) {
      digitalWrite(ledRGB, HIGH);
    } 
    else {
      digitalWrite(ledRGB, LOW);
    }
    break;

    //SUNSHINE
  case 11:
    digitalWrite(ledRGB, LOW);
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledBluPWM, LOW);
    for(int i=0; i<255; i++) {
      analogWrite(ledYelPWM, i);
      analogWrite(ledRedPWM, i/2);
      delay(30+ i/12);
      if(i == 150) {
        digitalWrite(ledYel, HIGH);
      }
    }
    digitalWrite(ledRed, HIGH);
    digitalWrite(ledWhi, HIGH);
    break;

    //RAIN
  case 12:
    digitalWrite(ledRed,LOW);
    digitalWrite(ledYel,LOW);
    digitalWrite(ledRedPWM,LOW);
    digitalWrite(ledYelPWM,LOW);
    digitalWrite(ledWhi, HIGH);
    digitalWrite(ledRGB, HIGH);
    for(int i=0; i<255; i++) {
      analogWrite(ledGrePWM, i/2);
      analogWrite(ledBluPWM, i);
      delay(30 + i/16);
    }
    break;

    //LIGHTNING
  case 13:
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledYel, LOW);
    digitalWrite(ledRed, LOW);
    analogWrite(ledBluPWM, 255);
    analogWrite(ledYelPWM, 10);
    analogWrite(ledRedPWM, 75);
    for(int i = 0; i<3; i++) {
      delay(300+random(200));
      digitalWrite(ledWhi, HIGH);
      delay(50+random(200));
      digitalWrite(ledWhi, LOW);
      delay(300+random(200));
      digitalWrite(ledWhi, HIGH);
      delay(150+random(200));
      digitalWrite(ledWhi, LOW);
      delay(1000+random(200));
      digitalWrite(ledRGB, HIGH);
      delay(50+random(200));
      digitalWrite(ledRGB, LOW);
      delay(400+random(200));
      digitalWrite(ledRGB, HIGH);
      digitalWrite(ledWhi, HIGH);
      delay(100+random(200));
      digitalWrite(ledRGB, LOW);
      digitalWrite(ledWhi, LOW);
      delay(100+random(200));
      digitalWrite(ledRGB, HIGH);
      delay(50+random(200));
      digitalWrite(ledRGB, LOW);
    }
    break;

    //RANDOM
  case 14:
    digitalWrite(ledBluPWM, LOW);
    digitalWrite(ledYelPWM, LOW);
    digitalWrite(ledRedPWM, LOW);
    digitalWrite(ledRGB, LOW);
    digitalWrite(ledRed, LOW);
    digitalWrite(ledWhi, LOW);
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledYel, LOW);
    if(random(200) > 100) {
      digitalWrite(ledWhi, HIGH);
    }
    delay(100);
    if(random(200) > 100) {
      digitalWrite(ledRGB, HIGH);
    }
    delay(100);
    if(random(200) > 100) {
      digitalWrite(ledYel, HIGH);
    }
    delay(100);
    if(random(200) > 100) {
      digitalWrite(ledRed, HIGH);
    }
    delay(100);
    analogWrite(ledBluPWM, random(255));
    delay(100);
    analogWrite(ledYelPWM, random(255));
    delay(100);
    analogWrite(ledRedPWM, random(255));
    delay(100);
    analogWrite(ledGrePWM, random(255));

    break;

    //MUSIC
  case 15:
    digitalWrite(ledBluPWM, LOW);
    digitalWrite(ledYelPWM, LOW);
    digitalWrite(ledRedPWM, LOW);
    digitalWrite(ledRGB, LOW);
    digitalWrite(ledRed, LOW);
    digitalWrite(ledWhi, LOW);
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledYel, LOW);
    if(random(200) > 100) {
      digitalWrite(ledWhi, HIGH);
    }
    if(random(200) > 100) {
      digitalWrite(ledRGB, HIGH);
    }
    if(random(200) > 100) {
      digitalWrite(ledYel, HIGH);
    }
    if(random(200) > 100) {
      digitalWrite(ledRed, HIGH);
    }
    analogWrite(ledBluPWM, random(255));
    analogWrite(ledYelPWM, random(255));
    analogWrite(ledRedPWM, random(255));
    analogWrite(ledGrePWM, random(255));
    updateInterval = 60000.0 / params;
    break;

    //SHUTDOWN
  case 21:
    digitalWrite(ledBluPWM, LOW);
    digitalWrite(ledYelPWM, LOW);
    digitalWrite(ledRedPWM, LOW);
    digitalWrite(ledRGB, LOW);
    digitalWrite(ledRed, LOW);
    digitalWrite(ledWhi, LOW);
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledYel, LOW);
    break;
  }
}

void updateAnimatedLight(int lastCase) {
  Serial.println("updateAnimatedLight");
  switch(lastCase) {
    //RAIN
  case 12: 
    {
      for(int i = 0; i<150; i++) {
        if(rainFadeIn == 0) {
          analogWrite(ledBluPWM, 150-i);
        } 
        else {
          analogWrite(ledBluPWM, i);
        }
        delay(50);
      }
      if(rainFadeIn == 0) {
        rainFadeIn = 1;
      } 
      else {
        rainFadeIn = 0;
      }
      break;
    }

    //LIGHTNING
  case 13:
    for(int i = 0; i<3; i++) {
      delay(300+random(200));
      digitalWrite(ledWhi, HIGH);
      delay(50+random(200));
      digitalWrite(ledWhi, LOW);
      delay(300+random(200));
      digitalWrite(ledWhi, HIGH);
      delay(100+random(200));
      digitalWrite(ledWhi, LOW);
      delay(1000+random(200));
      digitalWrite(ledRGB, HIGH);
      delay(50+random(200));
      digitalWrite(ledRGB, LOW);
      delay(400+random(200));
      digitalWrite(ledRGB, HIGH);
      digitalWrite(ledWhi, HIGH);
      delay(50+random(200));
      digitalWrite(ledRGB, LOW);
      digitalWrite(ledWhi, LOW);
      delay(100+random(200));
      digitalWrite(ledRGB, HIGH);
      delay(50+random(200));
      digitalWrite(ledRGB, LOW);
    }
    break;

    //MUSIC
  case 15:
    digitalWrite(ledBluPWM, LOW);
    digitalWrite(ledYelPWM, LOW);
    digitalWrite(ledRedPWM, LOW);
    digitalWrite(ledRGB, LOW);
    digitalWrite(ledRed, LOW);
    digitalWrite(ledWhi, LOW);
    digitalWrite(ledGrePWM, LOW);
    digitalWrite(ledYel, LOW);
    if(random(200) > 100) {
      digitalWrite(ledYel, HIGH);
    }
    if(random(200) > 100) {
      digitalWrite(ledRed, HIGH);
    }
    analogWrite(ledBluPWM, random(205));
    analogWrite(ledYelPWM, random(205));
    analogWrite(ledRedPWM, random(205));
    analogWrite(ledGrePWM, random(205));
    digitalWrite(ledRGB, HIGH);
    digitalWrite(ledWhi, HIGH);
    delay(25);
    digitalWrite(ledRGB,LOW);
    digitalWrite(ledWhi, LOW);
    if(beatCount % 8 == 0) {
      if(musicFast == 0) {
        updateInterval = updateInterval * 0.25;
        musicFast = 1;
      } 
      else {
        updateInterval = updateInterval * 4.0;
        musicFast = 0;
      }
    }
    beatCount++;
    break;
  }
}






















