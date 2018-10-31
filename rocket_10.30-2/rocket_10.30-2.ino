#include <SoftwareSerial.h>

char DELIM[] = {0xff, 0xff, 0xff, 0xff};

struct DATA_T {
  float flt1 = 1.01;
  float flt2 = 69.420;
  float flt3 = 468;
  float flt4 = 4;
  float flt5 = 4;
  float flt6 = 8;
  float flt7 = 16;
  float flt8 = 32;
} DATA;
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
  char *start = (char*) &DATA;
  for (int i = 0; i < DATA_BYTE_COUNT; i++) {
    XBee.write(*(start+ i));
  }
  XBee.write(DELIM);
}
