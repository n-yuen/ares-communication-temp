#include "gen.h"
extern void preUpdate();
extern float readImuX();
extern float readImuY();
extern float readImuZ();
extern unsigned int readSeries();

void updateData() {
	preUpdate();
	data.imuX = readImuX();
	data.imuY = readImuY();
	data.imuZ = readImuZ();
	data.series = readSeries();
}

