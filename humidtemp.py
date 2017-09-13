import smbus2
import bme280
import time

delay = 0.5
port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address)

# the compensated_reading class has the following attributes
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# there is a handy string representation too
print(data)


while True:
    data = bme280.sample(bus, address)
    print("{},{},{},{}".format(data.timestamp,data.temperature,data.pressure,data.humidity))
    time.sleep(delay)

