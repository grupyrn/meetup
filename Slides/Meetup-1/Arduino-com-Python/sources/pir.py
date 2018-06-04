from pyfirmata import Arduino, util
from pyfirmata import INPUT
import time

board = Arduino("/dev/cu.usbserial-AL008BFQ")
it = util.Iterator(board)
it.start()

board.digital[12].mode = INPUT
board.digital[12].enable_reporting()

while True:
    pir = board.digital[12].read()
    print(pir)
    board.pass_time(1)
    #time.sleep(1)

    if pir is True:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)

board.exit()
