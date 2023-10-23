#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM9DS1.h>
#include <Adafruit_BLE.h>
#include <Adafruit_BluefruitLE_SPI.h>
#include <BluefruitConfig.h>
#include <Adafruit_BluefruitLE_HID.h>

// Create an LSM9DS1 instance
Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();

// Create a Bluefruit instance
Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

// Create a HID instance
Adafruit_BluefruitLE_HID hid(ble);

// Sensitivity factors for accelerometer data
#define SENSITIVITY 2.0

void setup() {
  Serial.begin(115200);
  Serial.println("Feather 32u4 Bluefruit LE - 9-DOF IMU Mouse");

  if (!lsm.begin()) {
    Serial.println("Unable to start LSM9DS1. Check your wiring!");
    while (1);
  }
  
  lsm.setupAccel(lsm.LSMMODE_ACCEL_HIGH_RES | lsm.LSMMODE_ACCEL_952HZ);
  lsm.setupMag(lsm.LSMMODE_MAG_HIGH_RES | lsm.LSMMODE_MAG_80HZ);

  if (!ble.begin(VERBOSE_MODE)) {
    Serial.println("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?");
    while (1);
  }

  ble.factoryReset(); // Optional: remove any previously paired devices
  ble.setMode(BLUEFRUIT_MODE_DATA);

  ble.sendCommandCheckOK(F("AT+GAPDEVNAME=9-DOF IMU Mouse"));
  ble.sendCommandCheckOK(F("AT+BLEHIDEN=1"));

  Serial.println("Waiting for a connection...");
}

void loop() {
  if (ble.isConnected()) {
    lsm.read(); // Read accelerometer data

    int16_t x = lsm.accelData.x * SENSITIVITY;
    int16_t y = lsm.accelData.y * SENSITIVITY;

    hid.mouseMove(x, y); // Send the accelerometer data as mouse movement
  }

  delay(10); // Add a delay to avoid overwhelming the host device
}
