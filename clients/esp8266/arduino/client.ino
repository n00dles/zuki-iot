/*
ESP8266 ZUKI IOT Client.

TM36 temp client. 


*/

#include "ESP8266WiFi.h"

const char server[] = "192.168.0.x"; 

const char* MY_SSID = "ssid";
const char* MY_PWD =  "password";

WiFiClient client;

//TMP36 Pin Variables
int sensorPin = 0; 

void setup()
{
  Serial.begin(115200);
  Serial.print("Connecting to "+*MY_SSID);
  WiFi.begin(MY_SSID, MY_PWD);
  Serial.println("going into wl connect");

  while (WiFi.status() != WL_CONNECTED) //not connected,  ...waiting to connect
    {
      delay(1000);
      Serial.print(".");
    }
  Serial.println("wl connected");
  Serial.println("");
  Serial.println("Credentials accepted! Connected to wifi\n ");
  Serial.println("");
}

void loop() {

   // Wait a few seconds between measurements.
  delay(2000);

  //prefer to use float, but package size or float conversion isnt working
  //will revise in future with a string fuction or float conversion function

    int adc = analogRead(sensorPin); 
    float voltage = (((adc *3.3)/1024)-0.5)*100;

    Serial.println("\nStarting connection to server..."); 
  // if you get a connection, report back via serial:
  if (client.connect(server, 5000)) {
    Serial.println("connected to server");
    WiFi.printDiag(Serial);

    String data = "device=1&datai=1&data="+String(voltage)+"&hashkey=e2rD92si9jOQASuZqtmb";

     //change URL below if using your Sub-Domain
     client.println("POST /adddata HTTP/1.1"); 
     //change URL below if using your Domain
     client.print("Host: 192.168.0.277\n");                 
     client.println("User-Agent: ESP8266/1.0");
     client.println("Connection: close"); 
     client.println("Content-Type: application/x-www-form-urlencoded");
     client.print("Content-Length: ");
     client.print(data.length());
     client.print("\n\n");
     client.print(data);
     client.stop(); 
     
     Serial.println("\n");
     Serial.println("My data string im POSTing looks like this: ");
     Serial.println(data);
     Serial.println("And it is this many bytes: ");
     Serial.println(data.length());       
     delay(30000);
    } 

}


void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}