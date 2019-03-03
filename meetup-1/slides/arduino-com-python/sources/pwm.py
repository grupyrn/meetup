from pyfirmata import Arduino
from pyfirmata import PWM

board = Arduino("/dev/cu.usbserial-AL008BFQ")

board.digital[10].mode = PWM

for i in range(100):
    print(i)
    board.digital[10].write(i / 100.0)
    board.pass_time(0.05)
