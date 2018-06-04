from pyfirmata import Arduino
from time import sleep

# Arduino IDE
board = Arduino("/dev/cu.usbserial-AL008BFQ")

while True:
    # digitalWrite(13, 1);
    board.digital[13].write(1)
    # delay(1000);
    sleep(1)
    # digitalWrite(13, 0);
    board.digital[13].write(0)
    # delay(1000);
    sleep(1)
