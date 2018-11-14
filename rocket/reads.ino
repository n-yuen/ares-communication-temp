void preUpdate() {
    delay(random(500, 2000));
    //put whatever initialization you need before updating
}
//make sure the method signatures fit "gen.ino"
float readImuX () {
    return 0;
} 
float readImuY () {
    return 1;
}
float readImuZ () {
    return (float)sin(millis() / 2000.0);
    //return 2;
}
