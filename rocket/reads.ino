void preUpdate() {
    //put whatever initialization you need before updating
}
//make sure the method signatures fit "gen.ino"
float readImuX () {
    return 420.69;
} 
float readImuY () {
    return 2;
}
float readImuZ () {
    return (float)sin(millis() / 1000 * PI);
}
unsigned int series = 0;
unsigned int readSeries () {
    return series++;
}