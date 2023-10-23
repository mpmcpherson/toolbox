// COMMON SETTINGS
#define BLUEFRUIT_SPI_CS               8
#define BLUEFRUIT_SPI_IRQ              7
#define BLUEFRUIT_SPI_RST              4

#define VERBOSE_MODE                   true
#define BLE_READPACKET_TIMEOUT         500

#define BLUEFRUIT_SPI_SCK              SCK
#define BLUEFRUIT_SPI_MISO             MISO
#define BLUEFRUIT_SPI_MOSI             MOSI

// SOFTWARE SPI SETTINGS
// SCK, MISO and MOSI should be configured to match your hardware setup
#define SOFTWARE_SPI_SCK_PIN           13
#define SOFTWARE_SPI_MISO_PIN          12
#define SOFTWARE_SPI_MOSI_PIN          11

// HARDWARE SPI SETTINGS
// SCK, MISO and MOSI should be left as-is to use hardware SPI
#define SCK_LED                        LED_BUILTIN
#define MISO_LED                       LED_BUILTIN
#define MOSI_LED                       LED_BUILTIN

#endif // _BLUEFRUIT_CONFIG_H_
