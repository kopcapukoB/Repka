import RPi.GPIO as GPIO
import time
import smbus

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт; {upper_data_byte:x}, Младший байт; {lower_data_byte:x}, Число: {number}")
        return number

    def sequential_counting_adc(self):
        number = -1
        while(GPIO.input(self.comp_gpio) == 0 and number < 255):
            number = number + 1
            GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, number))
            time.sleep(self.compare_time)
        reset_number = 0
        GPIO.output(self.bits_gpio, R2R_ADC.number_to_dac(self, reset_number))
        return number
    
    def get_voltage(self):
        return float(self.dynamic_range * MCP3021.get_number(self) / 256)

if __name__ == "__main__":
    dac = MCP3021(5.19, True)
    try:
        while True:
            try:
                #print(dac.sequential_counting_adc())
                voltage = dac.get_voltage()
                print(f"Напряжение: {voltage} В\n")
                time.sleep(1.0)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        dac.deinit()