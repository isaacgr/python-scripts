# ESP8266 Flash Repo

To store verified esp8266 firmware and instructions to flash it

```
ex.
esptool.py --port /dev/ttyUSB0 write_flash 0x01000 user1.bin
```

```
boot_v1.1.bin---------------->0x00000
user1.bin-------------------->0x01000
esp_init_data_default.bin---->0x7C000
blank.bin-------------------->0x7E000

```
