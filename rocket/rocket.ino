#include <SoftwareSerial.h>
#include "gen.h"

/**
 * Probably don't need to touch this, write all the polling from arduino 2 in reads.ino
**/

extern void updateData();
char DELIM[] = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
char *dataStart = (char*)&data;
const int DATA_BYTE_COUNT = sizeof(data);

//For Atmega328P's
// XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
// XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
SoftwareSerial XBee(2, 3); // RX, TX

void setup() {
	// Set up both ports at 9600 baud. This value is most important
	// for the XBee. Make sure the baud rate matches the config
	// setting of your XBee.
	XBee.begin(9600);
}

void loop() {
	updateData();
	XBee.write(DELIM);
	for (int i = 0; i < DATA_BYTE_COUNT; i++) {
		XBee.write(*(dataStart + i));
	}
}
