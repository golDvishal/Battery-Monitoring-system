import machine
import utime

# Constants
R1 = 1000  # Resistance value in ohms (adjust as per your resistor)

# ADC pin
adc = machine.ADC(26)  # Use ADC0 (GP26/A0)

# Function to read battery voltage
def read_battery_voltage():
    adc_value = adc.read_u16()  # Read ADC value
    adc_voltage = adc_value * (3.3 / 65535)  # Convert to voltage (3.3V reference)
    battery_voltage = adc_voltage / (R1 / (R1 + R1))  # Calculate battery voltage
    return battery_voltage

# Main loop to monitor voltage drop
while True:
    battery_voltage = read_battery_voltage()
    print("Battery Voltage: {:.2f} V".format(battery_voltage))
    utime.sleep(1)
