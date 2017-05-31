# restfulpi
system:~#”dmesg” to make sure no conflict pin function, and check serial port at “dmesg | grep serial”

Use minicom in minicom -D /dev/ttyS1 -b 9600 to debug
ls /dev/ttyO* to check all the ttyO serial ports

disable cape-universal to remove conflicting UART pins(http://elinux.org/Beagleboard:BeagleBone_Debian_Image_Migration#cape-universal)

Make sure to change uEnv.txt and make sure to enable BB_UART



#Steps
ssh debian@192.168.6.2
or
ssh debian@192.168.7.2

login:temppwd

sudo -i
type in password: temppwd

cd restfulpi
python restfulpi.py

Make sure it says (otherwise restart or panic)
```Initializing PN532 NFC Driver
Found PN532 with firmware version: 1.6
Hello GFL```


Things to check
1. Power for NFC board: both red + green lights on
2. Power for Gate: Check the LCD, check the blue circuit breaker is up, check red + black wire to make sure they are firmly attached in the circuit breaker(unscrew and screw it back if needed)
3. Round shape plug for the gate power source

