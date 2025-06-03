from machine import I2C, Pin, deepsleep
from utime import ticks_ms, sleep_ms
import time
from bno08x import *

I2C_SDA = Pin(47)
I2C_SCL = Pin(48)

i2c1 = I2C(0, scl=I2C_SCL, sda=I2C_SDA, freq=100000, timeout=200000)

bno = BNO08X(i2c1, debug=False)
bno.enable_feature(BNO_REPORT_LINEAR_ACCELERATION, 20)
bno.calibration()

while True:
    accel_x, accel_y, accel_z = bno.acc_linear
    print(
        "Acceleration\tX: {:+.4f}\tY: {:+.4f}\tZ: {:+.4f}\tm/s²".format(
            accel_x, accel_y, accel_z
        )
    )

    # time.sleep(0.5)

"""
deepsleep duerme al ESP32 al mínimo consumo de energía, al despertar se reinicia por completo el ESP32

deepsleep() duerme de manera indefinida, hasta que una interrupción externa lo despierte
deepsleep(x) duerme por x milisegundos
"""
