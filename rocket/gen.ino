#include "gen.h"
extern void preUpdate();
extern float readImuX();
extern float readImuY();
extern float readImuZ();

void updateData() {
	preUpdate();
	data.imuX = readImuX();
	data.imuY = readImuY();
	data.imuZ = readImuZ();
}

