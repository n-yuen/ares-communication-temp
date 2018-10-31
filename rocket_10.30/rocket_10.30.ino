#include <SoftwareSerial.h>

char DELIM[] = {0xff, 0xff, 0xff, 0xff};

float DATA[] = {1.01, 3.1415926535897932384626, 69.420, 13.37, 2.999999999, 32, 64, 128};
const int DATA_BYTE_COUNT = sizeof(DATA);

//For Atmega328P's
// XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
// XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
SoftwareSerial XBee(2, 3); // RX, TX

void setup(){

  // Set up both ports at 9600 baud. This value is most important
  // for the XBee. Make sure the baud rate matches the config
  // setting of your XBee.
  XBee.begin(9600);
}

void loop(){
  XBee.write(DELIM);
  for (int i = 0; i < DATA_BYTE_COUNT/4; i++) {
    char* start = (char*) &(DATA[i]);
    XBee.write(*(start + 3));
    XBee.write(*(start + 2));
    XBee.write(*(start + 1));
    XBee.write(*start);
  }
  XBee.write(DELIM);
}
