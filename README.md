# restfulpi
system:~#”dmesg” to make sure no conflict pin function, and check serial port at “dmesg | grep serial”

Use minicom in minicom -D /dev/ttyS1 -b 9600 to debug
ls /dev/ttyO* to check all the ttyO serial ports

disable cape-universal to remove conflicting UART pins(http://elinux.org/Beagleboard:BeagleBone_Debian_Image_Migration#cape-universal)

Make sure to change uEnv.txt and make sure to enable BB_UART